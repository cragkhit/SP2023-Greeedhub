# Copyright 2018 Davide Spadini
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import logging
import os
from _datetime import datetime
from typing import List
from enum import Enum

from git import Repo, Diff, Git, Commit as GitCommit


logger = logging.getLogger(__name__)
from pydriller.domain.developer import Developer

NULL_TREE = '4b825dc642cb6eb9a060e54bf8d69288fbee4904'


class ModificationType(Enum):
    ADD = 1,
    COPY = 2,
    RENAME = 3,
    DELETE = 4,
    MODIFY = 5


class Modification:
    def __init__(self, old_path: str, new_path: str,
                 change_type: ModificationType, parents: List[str],
                 hash: str, path: str = None,
                 modifications_list=None):
        """
        Initialize a modification. A modification carries on information regarding
        the changed file.

        :param old_path: old path of the file (can be null if the file is added)
        :param new_path: new path of the file (can be null if the file is deleted)
        :param change_type: type of the change
        :param parents: type of the change
        :param hash
        :param path
        :param modifications_list
        """

        self.old_path = old_path
        self.new_path = new_path
        self.change_type = change_type
        self.filename = self._get_filename()
        self._parents = parents
        self._hash = hash
        self._path = path
        self._modifications_list = modifications_list

    @property
    def diff(self):
        key = '{},{}'.format(self.old_path, self.new_path)
        if self._modifications_list[key][0] is None:
            self.save_diff_and_sc()

        return self._modifications_list[key][0]

    @property
    def source_code(self):
        key = '{},{}'.format(self.old_path, self.new_path)
        if self._modifications_list[key][1] is None:
            self.save_diff_and_sc()

        return self._modifications_list[key][1]

    def save_diff_and_sc(self):
        repo = Repo(self._path)
        commit = repo.commit(self._hash)
        if len(self._parents) > 0:
            # the commit has a parent
            parent = repo.commit(self._parents[0])
            diff_index = parent.diff(commit, create_patch=True)
        else:
            # this is the first commit of the repo. Comparing it with git NULL TREE
            parent = repo.tree(NULL_TREE)
            diff_index = parent.diff(commit.tree, create_patch=True)
        self._parse_diff(diff_index)

    def _parse_diff(self, diff_index):
        for d in diff_index:
            old_path = d.a_path
            new_path = d.b_path
            diff = ''
            sc = ''
            try:
                diff = d.diff.decode('utf-8')
                sc = d.b_blob.data_stream.read().decode('utf-8')
            except (UnicodeDecodeError, AttributeError, ValueError):
                logger.debug('Could not load source code or the diff of a file in commit {}'.format(self._hash))

            key = '{},{}'.format(old_path ,new_path)
            self._modifications_list[key] = (diff, sc)

    @property
    def added(self):
        added = 0
        for line in self.diff.replace('\r', '').split("\n"):
            if line.startswith('+') and not line.startswith('+++'):
                added += 1
        return added

    @property
    def removed(self):
        removed = 0
        for line in self.diff.replace('\r', '').split("\n"):
            if line.startswith('-') and not line.startswith('---'):
                removed += 1
        return removed

    def _get_filename(self) -> str:
        if self.new_path is not None and self.new_path != "/dev/null":
            path = self.new_path
        else:
            path = self.old_path

        if os.sep not in path:
            return path

        filename = path.split(os.sep)
        return filename[-1]

    def __eq__(self, other):
        if not isinstance(other, Modification):
            return NotImplemented
        elif self is other:
            return True
        else:
            return self.__dict__ == other.__dict__

    def __str__(self):
        return (
            'MODIFICATION\n' +
            'Old Path: {}\n'.format(self.old_path) +
            'New Path: {}\n'.format(self.new_path) +
            'Type: {}\n'.format(self.change_type.name) +
            'Diff: {}\n'.format(self.diff) +
            'Source code: {}\n'.format(self.source_code)
        )


class Commit:
    def __init__(self, commit: GitCommit, path: str, main_branch: str) -> None:
        """
        Create a commit object.

        :param commit
        :param path
        :param main_branch
        """
        self._c_object = commit
        self._path = path
        self._main_branch = main_branch

    @property
    def hash(self):
        return self._c_object.hexsha

    @property
    def author(self):
        return Developer(self._c_object.author.name, self._c_object.author.email)

    @property
    def committer(self):
        return Developer(self._c_object.committer.name, self._c_object.committer.email)

    @property
    def author_date(self):
        return self._c_object.authored_datetime

    @property
    def committer_date(self):
        return self._c_object.committed_datetime

    @property
    def author_timezone(self):
        return self._c_object.author_tz_offset

    @property
    def committer_timezone(self):
        return self._c_object.committer_tz_offset

    @property
    def msg(self):
        return self._c_object.message.strip()

    @property
    def parents(self):
        parents = []
        for p in self._c_object.parents:
            parents.append(p.hexsha)
        return parents

    @property
    def merge(self):
        return len(self._c_object.parents) > 1

    @property
    def modifications(self):
        repo = Repo(self._path)
        commit = repo.commit(self.hash)

        if len(self.parents) > 0:
            # the commit has a parent
            parent = repo.commit(self.parents[0])
            diff_index = parent.diff(commit)
        else:
            # this is the first commit of the repo. Comparing it with git NULL TREE
            parent = repo.tree(NULL_TREE)
            diff_index = parent.diff(commit.tree)

        return self._parse_diff(diff_index)

    def _parse_diff(self, diff_index) -> List[Modification]:
        modifications_list = []
        modifications_list_w_sc = {}
        for d in diff_index:
            old_path = d.a_path
            new_path = d.b_path
            change_type = self._from_change_to_modification_type(d)

            if change_type == ModificationType.ADD:
                old_path = None
            elif change_type == ModificationType.DELETE:
                new_path = None

            key = '{},{}'.format(old_path, new_path)
            modifications_list_w_sc[key] = (None,None)
            modifications_list.append(Modification(old_path, new_path, change_type, self.parents, self.hash,
                                                   self._path, modifications_list_w_sc))
        return modifications_list

    @property
    def in_main_branch(self):
        return self._main_branch in self.branches

    @property
    def branches(self):
        git = Git(self._path)
        branches = set()
        for branch in set(git.branch('--contains', self.hash).split('\n')):
            branches.add(branch.strip().replace('* ', ''))
        return branches

    def _from_change_to_modification_type(self, d: Diff):
        if d.change_type == 'A':
            return ModificationType.ADD
        elif d.change_type == 'D':
            return ModificationType.DELETE
        elif d.change_type.startswith('R'):
            return ModificationType.RENAME
        elif d.change_type == 'M':
            return ModificationType.MODIFY

    def __eq__(self, other):
        if not isinstance(other, Commit):
            return NotImplemented
        elif self is other:
            return True
        else:
            return self.__dict__ == other.__dict__

    def __str__(self):
        return ('Hash: {}'.format(self.hash) + '\n'
                'Author: {}'.format(self.author.name) + '\n'
                'Author email: {}'.format(self.author.email) + '\n'
                'Committer: {}'.format(self.committer.name) + '\n'
                'Committer email: {}'.format(self.committer.email) + '\n'
                'Author date: {}'.format(self.author_date.strftime("%Y-%m-%d %H:%M:%S")) + '\n'
                'Committer date: {}'.format(self.committer_date.strftime("%Y-%m-%d %H:%M:%S")) + '\n'
                'Message: {}'.format(self.msg) + '\n'
                'Parent: {}'.format("\n".join(map(str, self.parents))) + '\n'
                'Merge: {}'.format(self.merge) + '\n'
                'Modifications: \n{}'.format("\n".join(map(str, self.modifications))) + '\n'
                'Branches: \n{}'.format("\n".join(map(str, self.branches))) + '\n'
                'In main branch: {}'.format(self.in_main_branch)
                )


class ChangeSet:
    def __init__(self, id: str, date: datetime):
        """
        Light-weight version of the commit, storing only the hash and the date. Used for filter out
        commits before asking for more complex information (like diff and source code).

        :param str id: hash of the commit
        :param date: date of the commit
        """
        self.id = id
        self.date = date

    def __eq__(self, other):
        if not isinstance(other, ChangeSet):
            return NotImplemented
        elif self is other:
            return True
        else:
            return self.__dict__ == other.__dict__

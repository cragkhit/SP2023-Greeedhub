"""
Module that calculates the number of commits made to a file.
"""

from pydriller import ModificationType, RepositoryMining
from pydriller.metrics.process.process_metric import ProcessMetric


class CommitsCount(ProcessMetric):
    """
    This class is responsible to implement the Commit Count metric to \
    measure the number of commits made to a file
    """

    def count(self):
        files = {}
        renamed_files = {}  # To keep track of renamed files

        for commit in RepositoryMining(path_to_repo=self.path_to_repo,
                                       from_commit=self.from_commit,
                                       to_commit=self.to_commit,
                                       reversed_order=True).traverse_commits():
            for modified_file in commit.modifications:

                filepath = renamed_files.get(modified_file.new_path,
                                             modified_file.new_path)
                if modified_file.change_type == ModificationType.RENAME:
                    renamed_files[modified_file.old_path] = filepath

                files[filepath] = files.get(filepath, 0) + 1

        return files

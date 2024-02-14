"""
Module that calculates the number of developers that contributed to each modified file \
in the repo in a given time range.

See https://dl.acm.org/doi/10.1145/2025113.2025119
"""
from pydriller.domain.commit import ModificationType
from pydriller.repository_mining import RepositoryMining
from pydriller.metrics.process.process_metric import ProcessMetric

class ContributorsCount(ProcessMetric):
    """
    This class is responsible to implement the following metrics:
    * Contributors Count: measures the number of contributors who modified a file.
    * Minor Contributors Count: measures the number of contributors who authored less \
        than 5% of code of a file.
    """

    def count(self):
        """
        Return the number of contributors who modified a file and those that authored \
        less than 5% of code for each modified file in the repository in the provided \
        time range [from_commit, to_commit]

        :return: dict 
            {filepath: {
                   contributors_count: int,
                   minor_contributors_count: int
                 }    
            }
        of number of contributors for each modified file
        """
        renamed_files = {}
        files = {}

        for commit in RepositoryMining(path_to_repo=self.path_to_repo,
                                       from_commit=self.from_commit,
                                       to_commit=self.to_commit,
                                       reversed_order=True).traverse_commits():

            for modified_file in commit.modifications:

                filepath = renamed_files.get(modified_file.new_path,
                                             modified_file.new_path)

                if modified_file.change_type == ModificationType.RENAME:
                    renamed_files[modified_file.old_path] = filepath

                author = commit.author.email.strip()
                lines_authored = modified_file.added + modified_file.removed

                files[filepath] = files.get(filepath, {})
                files[filepath][author] = files[filepath].get(author, 0) + lines_authored
        
        for path, contributions in list(files.items()):
            total = sum(contributions.values())
            if total == 0:
                del files[path]
            else:
                contributors_count = len(contributions.values())
                minor_contributors_count = sum(1 for v in contributions.values() if v/total < .05)

                files[path] = {
                    'contributors_count': contributors_count,
                    'minor_contributors_count': minor_contributors_count
                }

        print(files)
        return files

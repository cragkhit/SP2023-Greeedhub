import pytest
from pydriller.metrics.process.minor_contributors_count import MinorContributorsCount

TEST_DATA = [
   ('https://github.com/ishepard/pydriller', 'pydriller/git_repository.py', 'e9854bbea1cb7b7f06cbb559f7b06724d11ae1e5', 'e9854bbea1cb7b7f06cbb559f7b06724d11ae1e5', 0),
   ('https://github.com/ishepard/pydriller', 'pydriller/git_repository.py', None, 'e9854bbea1cb7b7f06cbb559f7b06724d11ae1e5', 1),
   ('https://github.com/ishepard/pydriller', 'pydriller/git_repository.py', None, '4af3839eb5ea5969f42142529a7a5526739fa570', 2)
]

@pytest.mark.parametrize('path_to_repo, filepath, from_commit, to_commit, expected', TEST_DATA)
def test(path_to_repo, filepath, from_commit, to_commit, expected):
    metric = MinorContributorsCount(path_to_repo=path_to_repo,
                                   from_commit=from_commit,
                                   to_commit=to_commit)
    count = metric.count()
    assert count[filepath] == expected

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

from pydriller.domain.commit import Modification, ModificationType

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

import pytest
from pathlib import Path
from pydriller.git_repository import GitRepository


@pytest.yield_fixture(scope="module")
def resource():
    yield GitRepository('test-repos/git-1/')


def test_equal(resource):
    c1 = resource.get_commit('e7d13b0511f8a176284ce4f92ed8c6e8d09c77f2')
    c2 = resource.get_commit(c1.parents[0])
    c3 = resource.get_commit('a4ece0762e797d2e2dcbd471115108dd6e05ff58')

    assert c1.parents[0] == 'a4ece0762e797d2e2dcbd471115108dd6e05ff58'
    assert c2 == c3
    assert c1 != c3


def test_filename():
    diff_and_sc = {
        'diff': '',
        'source_code': ''
    }
    m1 = Modification('dspadini/pydriller/myfile.py', 'dspadini/pydriller/mynewfile.py',
                      ModificationType.ADD, diff_and_sc)
    m3 = Modification('dspadini/pydriller/myfile.py', 'dspadini/pydriller/mynewfile.py',
                      ModificationType.ADD, diff_and_sc)
    m2 = Modification('dspadini/pydriller/myfile.py', None,
                      ModificationType.ADD, diff_and_sc)

    assert m1.filename == 'mynewfile.py'
    assert m2.filename == 'myfile.py'
    assert m1 != m2
    assert m1 == m3


def test_metrics_python():
    with open('test-repos/test6/git_repository.py') as f:
        sc = f.read()

    diff_and_sc = {
        'diff': '',
        'source_code': sc
    }

    m1 = Modification('test-repos/test6/git_repository.py', "test-repos/test6/git_repository.py",
                      ModificationType.MODIFY, diff_and_sc)

    assert 196 == m1.nloc
    assert 1009 == m1.token_count
    assert 43 == m1.complexity

    assert 19 == len(m1.methods)


def test_metrics_cpp():
    with open('test-repos/test6/FileCPP.cpp') as f:
        sc = f.read()

    diff_and_sc = {
        'diff': '',
        'source_code': sc
    }

    m1 = Modification('test-repos/test6/FileCPP.cpp', "test-repos/test6/FileCPP.cpp",
                      ModificationType.MODIFY, diff_and_sc)

    assert 332 == m1.nloc
    assert 2511 == m1.token_count
    assert 83 == m1.complexity

    assert 23 == len(m1.methods)


def test_metrics_java():
    with open('test-repos/test6/FileJava.java') as f:
        sc = f.read()

    diff_and_sc = {
        'diff': '',
        'source_code': sc
    }

    m1 = Modification('test-repos/test6/FileJava.java', "test-repos/test6/FileJava.java",
                      ModificationType.MODIFY, diff_and_sc)

    assert 466 == m1.nloc
    assert 3809 == m1.token_count
    assert 92 == m1.complexity

    assert 46 == len(m1.methods)


def test_metrics_not_supported_file():
    sc = 'asd !&%@*&^@\n jjdkj'

    diff_and_sc = {
        'diff': '',
        'source_code': sc
    }

    m1 = Modification('test-repos/test6/NotSupported.pdf', "test-repos/test6/NotSupported.pdf",
                      ModificationType.MODIFY, diff_and_sc)

    assert 2 == m1.nloc
    assert 0 == len(m1.methods)


def test_filepahs():
    gr = GitRepository('test-repos/test7')

    c = gr.get_commit('f0f8aea2db50ed9f16332d86af3629ff7780583e')

    mod0 = c.modifications[0]

    assert mod0.filename == 'a.java'

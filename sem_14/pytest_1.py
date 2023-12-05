import pytest

from task_1 import filter_string


@pytest.fixture
def result():
    return 'abc'


def test_no_changes(result):
    assert result == filter_string('abc')


def test_change_case(result):
    assert result == filter_string('Abc')


def test_remove_punct(result):
    assert result == filter_string('a.b.c')


def test_remove_other_alphs(result):
    assert result == filter_string('abcабв')


def test_complete_changes(result):
    assert result == filter_string('A.b.c.абв')



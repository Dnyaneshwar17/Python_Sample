import pytest

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")

@pytest.yield_fixture("class")
def class_level():
    print("class level setUp")

@pytest.yield_fixture("session")
def session_level():
    print("session level setUp")

@pytest.yield_fixture("module")
def module_level():
    print("module level setUp")



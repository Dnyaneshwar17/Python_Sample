
import pytest
import smtplib

@pytest.fixture(scope="module")
def smtp_connection():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
	
	@pytest.fixture(scope="session")
def smtp_connection():
    # the returned fixture value will be shared for
    # all tests needing it
    ...
	
#Higher-scoped fixtures are instantiated first¶	
@pytest.fixture(scope="session")
def s1():
    pass


@pytest.fixture(scope="module")
def m1():
    pass


@pytest.fixture
def f1(tmpdir):
    pass


@pytest.fixture
def f2():
    pass


def test_foo(f1, m1, f2, s1):
    ...	
	
	"""
	s1: is the highest-scoped fixture (session).
	m1: is the second highest-scoped fixture (module).
	"""
	
	

import pytest


@pytest.fixture(scope="function")
def prework():
    print("setup browser instance")

def test_initial_check(prework):
    print("Initial check")

def test_second_check(first_prework):
    print("Second check")



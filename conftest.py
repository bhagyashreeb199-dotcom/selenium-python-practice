import pytest


@pytest.fixture(scope="function")
def first_prework():
    print("setup browser instance")
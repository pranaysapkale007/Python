import pytest


@pytest.fixture()  # This will execute fixture before every test
def setup():
    print("This is fixture method. Wants before every method")


def test_method1(setup):
    print("This is method 1")


def test_method2(setup):
    print("This is method 2")

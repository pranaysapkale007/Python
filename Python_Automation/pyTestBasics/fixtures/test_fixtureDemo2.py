import pytest


@pytest.yield_fixture()  # This will execute fixture before and after every test
def setup():
    print("Once before every method")
    yield
    print("Once after every method")


def test_method1(setup):
    print("This is method 1")


def test_method2(setup):
    print("This is method 2")

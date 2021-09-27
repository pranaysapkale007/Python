import pytest


@pytest.mark.smoke
def test_login():
    print("Login Done")


@pytest.mark.regression
def test_addProduct():
    print("Product addition Done")


@pytest.mark.smoke
def test_logout():
    print("logout Done")



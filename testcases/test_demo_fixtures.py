import pytest


def test_Login_function():
    print("login Successfully")


@pytest.mark.Sanity
def test_Logout_function():
    print("logoff happened successfully")


@pytest.mark.Sanity
def test_addition():

    assert 2 + 2 == 5
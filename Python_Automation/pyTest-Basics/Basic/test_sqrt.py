import pytest
import conftest


def test_method1(setup):
    print(setup)
    print("This is method 1")


@pytest.mark.parametrize("num1,num2", [(10, 20), (20, 30)])
def test_method2(num1, num2):
    print("\n This is method 2 and parameters are : ", num1, num2)


def testdef():
    print("\n this is method 3")

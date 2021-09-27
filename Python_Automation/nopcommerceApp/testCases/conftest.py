from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C://Pranay//PythonWorkspace//Python_Automation//Driver"
                                                  "//chromedriver_win32//chromedriver.exe")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Ie()

    return driver


def pytest_addoption(parser):  # this method get value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return browser value to setup method
    return request.config.getoption("--browser")


##### pytest html report generation

# IT is hook for adding environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = "nop commerce"
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = 'Pranay'


# It is hook for delete/modify environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

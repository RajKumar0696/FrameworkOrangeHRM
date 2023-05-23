from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("This is chrome driver")

    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("This is firefox browser")
    else:
        driver = webdriver.Edge()
        print("This is edge browser")
    return driver


# This will get value from CLI

def pytest_addoption(parser):
    parser.addoption("--browser")


# This will return the browser value in set up method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# HTML report configuration

def pytest_configure(config):
    config._metadata['Project Name'] = 'OrangeHRM'
    config._metadata['Modual Name'] = 'Customer'
    config._metadata['Tester'] = 'Rajkumar'


# It is hooked for delete/modify Environment info to HTML Report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

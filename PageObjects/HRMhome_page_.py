import pytest


class HRMHomePage:
    def __init__(self, driver):
        self.driver = driver

    def get_home_page_title(self):
        return self.driver.title

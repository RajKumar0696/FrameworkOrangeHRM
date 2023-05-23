import pytest

from PageObjects.HRMlogin_page import LoginPage
from Utilities.read_properties import ReadConfig
from Utilities.custom_logger import LogGen


class Test_002_LogIn:
    base_url = ReadConfig.get_application_url()
    user_name = ReadConfig.get_user_name()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_login_page(self, setup):
        self.logger.info("**Test 002 Home page title check**")
        self.logger.info("**Login page title checking start**")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(5)

        self.login_page = LoginPage(self.driver)
        self.login_page.set_user_name(self.user_name)
        self.login_page.set_password(self.password)
        self.login_page.click_on_login()
        self.login_page.click_logout_drop_down()
        self.login_page.click_logout()
        self.logger.info("**Login test passed**")

        login_title = self.driver.title
        print(login_title)

        self.logger.info("**Login page validation start**")
        if login_title == "OrangeHRM":
            assert True
            print("Login test passed and title matched")
            self.logger.info("**Login test passed and title matched**")

        else:
            self.driver.save_screenshot(".\\ScreenShots\\"+"login_page.png")
            print("Login test failed and title not matched")
            self.logger.info("**Login test passed and title not matched**")
            assert False

import pytest

from Utilities.read_properties import ReadConfig
from Utilities.custom_logger import LogGen


class Test_001_HomePage:
    base_url = ReadConfig.get_application_url()
    user_name = ReadConfig.get_user_name()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_home_page_title(self, setup):
        self.logger.info("**Test 001 Home page title check**")
        self.logger.info("**Home page title checking start**")
        self.driver = setup
        self.driver.get(self.base_url)
        self.act_title = self.driver.title
        self.driver.implicitly_wait(5)

        self.logger.info("**Home page validation start**")
        if self.act_title == "OrangeHRM":
            assert True
            self.driver.close()
            print("Home page title test passed")
            self.logger.info("**Home page title test passed**")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "home_page.png")
            print("Home page title test failed")
            self.logger.info("**Home page title test failed**")
            self.driver.close()
            assert False

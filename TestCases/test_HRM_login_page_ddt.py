import time
import pytest

from PageObjects.HRMlogin_page import LoginPage
from Utilities.read_properties import ReadConfig
from Utilities.custom_logger import LogGen
from Utilities import XLutils


class Test_003_LogIn_DDT:
    base_url = ReadConfig.get_application_url()
    path = "TestData/OrangeHRM_test_report.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_login_page_ddt(self, setup):
        self.logger.info("**Test 003 Login page ddt test**")
        self.logger.info("**Login page title checking start**")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(5)
        self.login_page = LoginPage(self.driver)
        self.row = XLutils.getRowCount(self.path, 'Sheet1')
        print("Number of rows:", self.row)
        lst_status = []

        for r in range(2, self.row + 1):
            self.user_name = XLutils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLutils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLutils.readData(self.path, 'Sheet1', r, 3)

            self.login_page.set_user_name(self.user_name)
            self.login_page.set_password(self.password)
            self.login_page.click_on_login()
            time.sleep(5)
            self.logger.info("**Login test passed**")

            act_title = self.driver.title
            exp_title = "OrangeHRM"

            if act_title == exp_title:
                if self.exp == "pass":
                    self.logger.info("**Test passed**")
                    self.login_page.click_logout_drop_down()
                    self.login_page.click_logout()
                    lst_status.append("pass")
                elif self.exp == "fail":
                    self.logger.info("** Test failed**")
                    lst_status.append("fail")

            elif act_title != exp_title:
                if self.exp == "pass":
                    self.logger.info("** Test failed**")
                elif self.exp == "file":
                    self.logger.info("**Test passed**")

        if "fail" not in lst_status:
            self.logger.info("** DDT test passed**")
            self.driver.close()
            lst_status.append("pass")
            assert True
        elif "pass" not in lst_status:
            self.logger.info("** DDT test failed**")
            self.driver.close()
            lst_status.append("fail")
            assert False





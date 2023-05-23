from selenium.webdriver.common.by import By


class LoginPage:
    txt_user_name_xpath = "//input[@placeholder='Username']"
    txt_password_xpath = "//input[@placeholder='Password']"
    btn_login_xpath = "//button[normalize-space()='Login']"
    dro_logout_xpath = "//span[@class='oxd-userdropdown-tab']"
    lik_logout_xpath = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def set_user_name(self, user_name):
        self.driver.find_element(By.XPATH, self.txt_user_name_xpath).send_keys(user_name)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def click_on_login(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def click_logout_drop_down(self):
        self.driver.find_element(By.XPATH, self.dro_logout_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.lik_logout_xpath).click()


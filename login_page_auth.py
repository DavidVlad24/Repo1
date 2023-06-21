from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from browser import Browser

class LoginPage(Browser):
    USERNAME_INPUT = (By.XPATH, '//*[@id="username"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login"]/button')
    INVALID_USERNAME_MESSAGE = (By.XPATH, '//*[@id="flash"]"]')
    INVALID_PASSWORD_MESSAGE = (By.XPATH, '//*[@id="flash"]"]')
    SUCCESS_LOGIN_MESSAGE = (By.NAME, 'You logged into a secure area!')
    LOGOUT_BUTTON = (By.NAME, 'Logout')
    LOGOUT_MESSAGE = (By.NAME, 'You logged out of the secure area!')

    def navigate_to_form_auth(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def click_logout_button(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).click()

    def set_username(self, username):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def verify_invalid_username_message(self, expected_message):
        try:
            actual_message = self.driver.find_element(*self.INVALID_USERNAME_MESSAGE).text
        except NoSuchElementException:
            actual_message = "None"
        assert actual_message == expected_message, f"Error: The invalid username message is incorrect. Expected: '{expected_message}', Actual: '{actual_message}'"

    def verify_invalid_password_message(self, expected_message):
        try:
            actual_message = self.driver.find_element(*self.INVALID_PASSWORD_MESSAGE).text
        except NoSuchElementException:
            actual_message = "None"
        assert actual_message == expected_message, f"Error: The invalid password message is incorrect. Expected: '{expected_message}', Actual: '{actual_message}'"

    def success_login_message(self):
        self.driver.find_element(*self.SUCCESS_LOGIN_MESSAGE).is_displayed(), "Error, the success login message is not displayed"

    def logout_message(self):
        self.driver.find_element(*self.LOGOUT_MESSAGE).is_displayed(), "Error, the logout message is not displayed"


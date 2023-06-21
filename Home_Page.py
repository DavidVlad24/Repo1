from selenium.webdriver.common.by import By
from browser import Browser


class HomePage(Browser):
    CHECKBOX = (By.XPATH, '//*[@id="content"]/ul/li[6]/a')
    FORM_AUTH = (By.XPATH, '//*[@id="content"]/ul/li[21]/a')
    ADD_REMOVE_ELEMENTS = (By.XPATH, '//*[@id="content"]/ul/li[2]/a')

    def navigate_to_checkbox(self):
        self.driver.get("https://the-internet.herokuapp.com/")

    def click_on_checkbox(self):
        self.driver.find_element(*self.CHECKBOX).click()

    def check_url_checkbox(self):
        actual_url = "https://the-internet.herokuapp.com/checkboxes"
        expected_url = "https://the-internet.herokuapp.com/checkboxes"
        assert actual_url == expected_url, "Url is incorrect"

    def navigate_to_form_auth(self):
        self.driver.get("https://the-internet.herokuapp.com/")
    def click_on_form_auth(self):
        self.driver.find_element(*self.FORM_AUTH).click()

    def check_url_form_auth(self):
        actual_url = "https://the-internet.herokuapp.com/login"
        expected_url = "https://the-internet.herokuapp.com/login"
        assert actual_url == expected_url , "Url is incorrect"


    def navigate_to_add_remove_elements(self):
        self.driver.get("https://the-internet.herokuapp.com/")

    def click_on_add_remove_elements(self):
        self.driver.find_element(*self.ADD_REMOVE_ELEMENTS).click()

    def check_url_add_remove_elements(self):
        actual_url = "https://the-internet.herokuapp.com/add_remove_elements/"
        expected_url = "https://the-internet.herokuapp.com/add_remove_elements/"
        assert actual_url == expected_url, "Url is incorrect"



from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, """button""")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_HELLO = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_NEW_POST_BTN = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_DESCRIPTION = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_SAVE_POST_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button/span""")
    LOCATOR_NEW_POST_TITLE = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_CONTACT_US = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_YOUR_NAME_FEEDBACK = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_YOUR_EMAIL_FEEDBACK = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTENT_FEEDBACK = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button/span""")

class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} in element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} in element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        pass_field.clear()
        pass_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login buton")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def get_user_text(self):
        logging.info(f"Displaying a welcome message: Hello, {TestSearchLocators.LOCATOR_HELLO}")
        user_field = self.find_element(TestSearchLocators.LOCATOR_HELLO, time=2)
        text = user_field.text
        return text

    def click_new_post_btn(self):
        logging.info("Click button create new post")
        self.find_element(TestSearchLocators.LOCATOR_NEW_POST_BTN).click()

    def enter_title(self, word):
        logging.info(f"Send {word} in element {TestSearchLocators.LOCATOR_TITLE}")
        title_field = self.find_element(TestSearchLocators.LOCATOR_TITLE)
        title_field.clear()
        title_field.send_keys(word)

    def enter_description(self, word):
        logging.info(f"Send {word} in element {TestSearchLocators.LOCATOR_DESCRIPTION}")
        desc_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION)
        desc_field.clear()
        desc_field.send_keys(word)

    def enter_content(self, word):
        logging.info(f"Send {word} in element {TestSearchLocators.LOCATOR_CONTENT}")
        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT)
        content_field.clear()
        content_field.send_keys(word)

    def click_save_button(self):
        logging.info("Click save post button")
        self.find_element(TestSearchLocators.LOCATOR_SAVE_POST_BTN).click()

    def get_res_text(self):
        logging.info(f"Displaying a new post title {TestSearchLocators.LOCATOR_NEW_POST_TITLE}")
        res_field = self.find_element(TestSearchLocators.LOCATOR_NEW_POST_TITLE, time=2)
        text = res_field.text
        return text

    def click_contact_us(self):
        logging.info("Click contact us")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US).click()

    def get_name_feedback(self, word):
        logging.info(f"Send {word} in element {TestSearchLocators.LOCATOR_YOUR_NAME_FEEDBACK}")
        name_field = self.find_element(TestSearchLocators.LOCATOR_TITLE)
        name_field.clear()
        name_field.send_keys(word)

    def enter_name_feedback(self, word):
        logging.info(f"Send {word} in element {TestSearchLocators.LOCATOR_YOUR_NAME_FEEDBACK}")
        name_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_NAME_FEEDBACK)
        name_field.clear()
        name_field.send_keys(word)

    def enter_email_feedback(self, word):
        logging.info(f"Send {word} in element {TestSearchLocators.LOCATOR_YOUR_EMAIL_FEEDBACK}")
        name_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_EMAIL_FEEDBACK)
        name_field.clear()
        name_field.send_keys(word)

    def enter_content_feedback(self, word):
        logging.info(f"Send {word} in element {TestSearchLocators.LOCATOR_CONTENT_FEEDBACK}")
        name_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_FEEDBACK)
        name_field.clear()
        name_field.send_keys(word)

    def click_contact_us_button(self):
        logging.info("Click contact us button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()

    def get_alert(self):
        alert = self.driver.switch_to.alert
        return alert.text



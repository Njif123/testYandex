import time

from selenium.webdriver.common.by import By

from fw.web_base import WebBase


class Locator:
    button_email = (By.XPATH, '//button[@data-type="login"]')
    input_email = (By.ID, 'passp-field-login')
    button_phone = (By.XPATH, '//button[@data-type="phone"]')
    input_phone = (By.ID, 'passp-field-phone')
    input_password = (By.ID, 'passp-field-passwd')
    button_sign_in = (By.ID, 'passp:sign-in')
    current_user_profile_button = (By.XPATH, '//button[@class="UserID-Account"]')
    span_user_login = (By.XPATH, '//span[contains(@class,"UserId-SecondLine")]')
    div_login_hint = (By.ID, 'field:input-login:hint')
    div_phone_hint = (By.ID, 'field:input-phone:hint')
    div_password_hint = (By.ID, 'field:input-passwd:hint')


class AuthorizationPage(WebBase):

    def open_authorization_page(self):
        self.get_driver().get('https://passport.yandex.ru/')

    def fill_login_field(self, login):
        # на вход можно передавать логин или email
        self.click_element(Locator.button_email)
        self.click_element(Locator.input_email)
        self.send_keys(Locator.input_email, login)
        return self

    def click_button_sign_in(self):
        self.click_element(Locator.button_sign_in)
        return self

    def fill_password_field(self, password):
        self.click_element(Locator.input_password)
        self.send_keys(Locator.input_password, password)
        return self

    def fill_phone_field(self, phone):
        self.click_element(Locator.button_phone)
        self.click_element(Locator.input_phone)
        self.send_keys(Locator.input_phone, phone)
        return self

    def check_current_user(self, email):
        self.click_element(Locator.current_user_profile_button)
        time.sleep(5)
        self.find_element(Locator.span_user_login)
        user_login = self.get_tag_text(Locator.span_user_login)
        email = email.split('@')[0]
        if user_login.lower() == email.lower():
            return True
        else:
            return False

    def check_error_hint_login(self):
        return self.check_is_there_element_on_the_page(Locator.div_login_hint)

    def check_error_hint_password(self):
        return self.check_is_there_element_on_the_page(Locator.div_password_hint)

    def check_error_hint_phone(self):
        return self.check_is_there_element_on_the_page(Locator.div_phone_hint)


from tests.web_tests.web_test_base import WebTestBase


class TestWebAuthorization(WebTestBase):

    def setup_class(self):
        self.user_id = 1
        # Получаем логин и пароль пользователя
        self.email_and_password = self.APP.users.get_user_email_and_password_by_id(self.user_id)

    def setup_method(self):
        # Открываем страницу авторизации
        self.APP.authorization_page.open_authorization_page()

    def test_correct_email_and_password(self):
        # Заполняем поле "Логин"
        self.APP.authorization_page.fill_login_field(self.email_and_password['email'])
        # Нажимаем на кнопку "Войти"
        self.APP.authorization_page.click_button_sign_in()
        # Заполняем поле "Пароль"
        self.APP.authorization_page.fill_password_field(self.email_and_password['password'])
        # Нажимаем на кнопку "Войти"
        self.APP.authorization_page.click_button_sign_in()
        # Проверяем текущего пользователя
        assert self.APP.authorization_page.check_current_user(self.email_and_password['email'])

    def test_incorrect_email(self):
        # Заполняем поле "Логин"
        self.APP.authorization_page.fill_login_field(self.email_and_password['email']+'fail')
        # Нажимаем на кнопку "Войти"
        self.APP.authorization_page.click_button_sign_in()
        # Проверяем появление ошибки
        assert self.APP.authorization_page.check_error_hint_login()

    def test_correct_email_incorrect_password(self):
        # Заполняем поле "Логин"
        self.APP.authorization_page.fill_login_field(self.email_and_password['email'])
        # Нажимаем на кнопку "Войти"
        self.APP.authorization_page.click_button_sign_in()
        # Заполняем поле "Пароль"
        self.APP.authorization_page.fill_password_field(self.email_and_password['password']+'fail')
        # Нажимаем на кнопку "Войти"
        self.APP.authorization_page.click_button_sign_in()
        # Проверяем появление ошибки
        assert self.APP.authorization_page.check_error_hint_password()

    def test_incorrect_phone(self):
        # Получаем номер телефона пользователя
        user_phone = self.APP.users.get_user_phone_number_by_id(self.user_id)
        # Заполняем поле "Логин"
        self.APP.authorization_page.fill_phone_field(user_phone)
        # Нажимаем на кнопку "Войти"
        self.APP.authorization_page.click_button_sign_in()
        # Проверяем появление ошибки
        assert self.APP.authorization_page.check_error_hint_phone()

    def test_incorrect_login(self):
        # Получаем логин пользователя
        user_login = self.APP.users.get_user_login_by_id(self.user_id)
        # Заполняем поле "Логин"
        self.APP.authorization_page.fill_login_field(user_login+'fail')
        # Нажимаем на кнопку "Войти"
        self.APP.authorization_page.click_button_sign_in()
        # Проверяем появление ошибки
        assert self.APP.authorization_page.check_error_hint_login()


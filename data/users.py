import requests


class Users:

    # Получение списка пользователей
    def get_users(self):
        response = requests.get('https://jsonplaceholder.typicode.com/users')

        users = response.json()

        return users

    def get_user_email_and_password_by_id(self, user_id):
        # Получение логина и пароля для входа по email
        users = self.get_users()
        login_and_password = {}
        for user in users:
            if user['id'] == user_id:
                login_and_password['email'] = user['email']
                login_and_password['password'] = user['website']
        return login_and_password

    def get_user_phone_number_by_id(self, user_id):
        # Получение номера телефона для входа
        users = self.get_users()
        for user in users:
            if user['id'] == user_id:
                phone = user['phone']
        return phone

    def get_user_login_by_id(self, user_id):
        # Получение логина для входа
        users = self.get_users()
        for user in users:
            if user['id'] == user_id:
                login = user['username']
        return login



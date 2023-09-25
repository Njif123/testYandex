from data.users import Users
from fw.authorization_page import AuthorizationPage
from fw.web_base import WebBase


class ApplicationManager:

    def __init__(self):
        self.web_base = WebBase()
        self.authorization_page = AuthorizationPage()
        self.users = Users()

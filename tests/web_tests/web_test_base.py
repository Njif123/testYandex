from tests.test_base import TestBase


class WebTestBase(TestBase):

    def setup_class(self):
        pass

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def teardown_class(self):
        self.APP.web_base.quit_driver()

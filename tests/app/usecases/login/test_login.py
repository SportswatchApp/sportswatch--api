from rest_framework.authtoken.models import Token

from app.models import User
from app.usecases import login
from tests.app.usecases.testcase import UseCaseTestCase


class TestLogin(UseCaseTestCase):

    def setUp(self) -> None:
        super().setUp()

    def test_when_email_not_valid(self):
        self.request = self.create_request({
            'email': 'invalid',
            'password': ''
        })
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_invalid_request)

    def test_when_invalid_credentials(self):
        self.request = self.create_request({
            'email': 'dd@dd.com',
            'password': 'qwerty'
        })
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_invalid_credentials)

    def test_when_valid_credentials_Should_give_token(self):
        User.objects.create_user(
            username='u@u.dk',
            password='qwerty'
        )
        self.request = self.create_request({
            'email': 'u@u.dk',
            'password': 'qwerty'
        })
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_success)

    def test_when_user_already_logged_in_Should_give_token(self):
        user = User.objects.create_user(
            username='u@u.dk',
            password='qwerty'
        )
        Token.objects.create(user=user)  # log user in
        self.request = self.create_request({
            'email': 'u@u.dk',
            'password': 'qwerty'
        })
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_success)

    def run_use_case(self):
        login.Login.login(self.request, self.listener)

    def create_request(self, fields):
        return login.Request().from_dict(fields)

from django.contrib.auth.models import AnonymousUser
from rest_framework.authtoken.models import Token

from app.models import User
from app.usecases import logout
from tests.app.usecases.testcase import UseCaseTestCase


class TestLogout(UseCaseTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User.objects.create_user(
            username='qwerty',
            password='qwerty'
        )

    def test_when_user_is_anonymous(self):
        self.user = AnonymousUser()
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_anonymous_user)

    def test_user_can_successfully_log_out(self):
        Token.objects.create(user=self.user)
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_success)
        self.assertEqual(0, Token.objects.count())

    def test_user_can_successfully_log_out_no_token(self):
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_success)
        self.assertEqual(0, Token.objects.count())

    def create_request(self, fields):
        pass

    def run_use_case(self):
        logout.Logout.logout(self.user, self.listener)

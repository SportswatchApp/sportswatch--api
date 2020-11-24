from app.models import User
from tests.app.endpoints.testcase import EndpointTestCase


class TestCreateUserEndpoint(EndpointTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.url = 'v1/users/'

    def test_when_no_data_provided_Should_get_bad_request(self):
        body = {}
        response = self.unauthorized_client.post(self.get_url(), data=self.to_json(body))
        self.assertEquals(400, response.status_code)

    def test_when_passwords_are_not_identical_Should_get_bad_request(self):
        body = {
            "email": "test@test.com",
            "first_name": "John",
            "last_name": "string",
            "password": "password123",
            "conf_password": "123password"
        }
        response = self.unauthorized_client.post(self.get_url(), data=self.to_json(body))
        expected = {'detail': 'Passwords are not identical', 'status': 400}
        self.assertDictEqual(expected, self.get_response_body(response))

    def test_when_email_already_in_use_Should_get_conflict(self):
        self.User.create(
            username='test@test.com'
        )
        body = {
            "email": "test@test.com",
            "first_name": "John",
            "last_name": "string",
            "password": "qwerty12",
            "conf_password": "qwerty12"
        }
        response = self.unauthorized_client.post(self.get_url(), data=self.to_json(body))
        expected = {'detail': 'E-mail already in use', 'status': 409}
        actual = self.get_response_body(response)
        self.assertDictEqual(expected, actual)
        self.assertEquals(409, response.status_code)

    def test_can_create_user_successfully(self):
        body = {
            "email": "test@test.com",
            "first_name": "John",
            "last_name": "string",
            "password": "qwerty12",
            "conf_password": "qwerty12"
        }
        response = self.unauthorized_client.post(self.get_url(), data=self.to_json(body))
        actual = self.get_response_body(response)
        expected = User.objects.get(username='test@test.com').__dto__()
        self.assertDictEqual(expected, actual)
        self.assertEquals(201, response.status_code)

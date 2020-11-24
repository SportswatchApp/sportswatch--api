from tests.app.endpoints.testcase import EndpointTestCase


class TestLoginEndpoint(EndpointTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = self.User.create(
            username='dd@dd.com',
            password='qwerty'
        )
        self.url = 'v1/login/'

    def test_when_body_invalid_Should_get_bad_request(self):
        body = {
            'email': 'usernmae'
        }
        response = self.unauthorized_client.post(self.get_url(), data=self.to_json(body))
        expected = {'detail': 'Missing required field: password', 'status': 400}
        self.assertDictEqual(expected, response.data)
        self.assertEquals(400, response.status_code)

    def test_when_email_not_valid_Should_get_bad_request(self):
        body = {
            'email': 'usernmae',
            'password': 'qwerty'
        }
        response = self.unauthorized_client.post(self.get_url(), data=self.to_json(body))
        expected = {'detail': 'Email address is not valid', 'status': 400}
        self.assertDictEqual(expected, response.data)
        self.assertEquals(400, response.status_code)

    def test_when_credentials_wrong_Should_get_forbidden(self):
        body = {
            'email': 'dd@dd.com',
            'password': 'wrong password'
        }
        response = self.unauthorized_client.post(self.get_url(), data=self.to_json(body))
        expected = {'detail': 'Invalid credentials', 'status': 401}
        self.assertDictEqual(expected, response.data)
        self.assertEquals(401, response.status_code)

    def test_can_login_successfully(self):
        body = {
            'email': 'dd@dd.com',
            'password': 'qwerty'
        }
        response = self.unauthorized_client.post(self.get_url(), data=self.to_json(body))
        self.assertIn('token', response.data)
        self.assertIn('created', response.data)
        self.assertEquals(202, response.status_code)

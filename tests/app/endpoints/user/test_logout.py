from tests.app.endpoints.testcase import EndpointTestCase


class TestLogoutEndpoint(EndpointTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.url = 'v1/logout/'

    def test_when_token_not_provided_Cannot_log_out(self):
        response = self.unauthorized_client.post(self.get_url())
        self.assertAuthenticationFailed(response)

    def test_can_logout_successfully(self):
        response = self.client.post(self.get_url())
        body = self.get_response_body(response)
        expected = {'detail': 'User logged out'}
        self.assertDictEqual(expected, body)
        self.assertEquals(205, response.status_code)

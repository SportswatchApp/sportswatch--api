from tests.app.endpoints.testcase import EndpointTestCase


class TestGetUserEndpoint(EndpointTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.url = 'v1/user/'

    def test_when_does_not_exist(self):
        response = self.client.get(self.get_url())
        actual = self.get_response_body(response)
        expected = self.client.authorized_user.__dto__()
        self.assertDictEqual(expected, actual)

    def test_when_user_not_authorized(self):
        response = self.unauthorized_client.get(self.get_url())
        self.assertAuthenticationFailed(response)

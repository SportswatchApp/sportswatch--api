from tests.app.endpoints.testcase import EndpointTestCase


class TestApplyMembershipView(EndpointTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.url = '/api/v1/club/1/apply/'

    def test_when_user_not_logged_in_Should_get_401(self):
        response = self.unauthorized_client.post(self.url)
        self.assertEqual(401, response.status_code)

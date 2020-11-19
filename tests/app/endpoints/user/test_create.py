from unittest import mock
from app.usecases.create_user import Listener
from tests.app.endpoints.testcase import EndpointTestCase


class TestCreateUserEndpoint(EndpointTestCase):

    def test_when_no_data_provided_Should_get_bad_request(self):
        response = self.client.post('/api/v1/users/')
        self.assertEqual(400, response.status_code)

    def test_when_user_already_exist_Should_get_already_reported(self):
        with mock.patch.object(Listener, 'get_response') as m:
            m.return_value = (403, '')
            response = self.client.post('/api/v1/users/')
            self.assertEqual(403, response.status_code)

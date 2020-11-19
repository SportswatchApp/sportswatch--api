from unittest import mock

from django.test import client
from parameterized import parameterized

from app.usecases import create_time
from tests.app.endpoints.testcase import EndpointTestCase


class TestCreateTimeEndpoint(EndpointTestCase):

    def test_when_user_not_logged_in_Should_get_401(self):
        self.client = client.Client()
        response = self.client.post('/api/v1/time/')
        self.assertEqual(401, response.status_code)

    @parameterized.expand([
        [400],
        [403],
        [404]
    ])
    def test_can_get_status_codes_responses(self, status_code):
        with mock.patch.object(create_time.Listener, 'get_response') as m:
            m.return_value = (status_code, '')
            response = self.client.post('/api/v1/time/')
            self.assertEqual(status_code, response.status_code)

import json
from tests.object_environment.factory import EnvironmentFactory
from django.test import TestCase
from django.test import client
from tests.app.endpoints.api_client import ApiClient


class EndpointTestCase(TestCase, EnvironmentFactory):

    def setUp(self) -> None:
        client.MULTIPART_CONTENT = 'application/json'
        self.client = ApiClient()
        self.unauthorized_client = client.Client()
        self.url = ''

    def to_json(self, _dict):
        return json.dumps(_dict)

    def get_response_body(self, response):
        return self.from_json(response._container[0].decode('utf-8'))

    def from_json(self, _json):
        return json.loads(_json)

    def get_url(self, path_parameters={}):
        path = '/api/' + self.url
        for key in path_parameters:
            path_variable = '{' + key + '}'
            path = path.replace(path_variable, str(path_parameters[key]))
        return path

    def assertAuthenticationFailed(self, response):
        actual = self.get_response_body(response)
        expected = {'detail': 'Authentication credentials were not provided.'}
        self.assertDictEqual(expected, actual)
        self.assertEquals(401, response.status_code)

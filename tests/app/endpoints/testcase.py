from django.test import TestCase
from django.test import client
from tests.app.endpoints.api_client import ApiClient


class EndpointTestCase(TestCase):

    def setUp(self) -> None:
        client.MULTIPART_CONTENT = 'application/json'
        self.client = ApiClient()
        self.unauthorized_client = client.Client()

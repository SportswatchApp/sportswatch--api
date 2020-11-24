from app.models import Club
from tests.app.endpoints.testcase import EndpointTestCase


class TestListClubsEndpoint(EndpointTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.url = 'v1/clubs/'

    def test_can_list_clubs(self):
        clubs = [
            self.Club.create(),
            self.Club.create()
        ]
        response = self.client.get(self.get_url())
        self.assertDictEqual(Club.__dtolist__(clubs), self.get_response_body(response))
        self.assertEquals(200, response.status_code)

from app.models import Club
from tests.app.endpoints.testcase import EndpointTestCase


class TestCreateClubEndpoint(EndpointTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.url = 'v1/club/'

    def test_when_body_is_invalid_Should_get_bad_request(self):
        body = {
            'name': 'GymClub',
            'region': 'Nordjylland',
            'zip_code': 9000,
            'city': 'Aalborg',
        }
        response = self.client.post(self.get_url(), data=body)
        expected = {'detail': 'Missing required field: country', 'status': 400}
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEquals(400, response.status_code)

    def test_when_club_already_exists_Should_get_conflict(self):
        body = {
            'name': 'GymClub',
            'region': 'Nordjylland',
            'zip_code': 9000,
            'city': 'Aalborg',
            'country': 'Danmark'
        }
        self.Club.create(**body)
        response = self.client.post(self.get_url(), data=body)
        expected = {'detail': 'The club already exist', 'status': 409}
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEquals(409, response.status_code)

    def test_can_create_club_success(self):
        body = {
            'name': 'GymClub',
            'region': 'Nordjylland',
            'zip_code': '9000',
            'city': 'Aalborg',
            'country': 'Danmark'
        }
        response = self.client.post(self.get_url(), data=body)
        expected = Club.objects.get(name='GymClub').__dto__()
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEquals(201, response.status_code)

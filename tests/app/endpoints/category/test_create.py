from app.models import Category, Club, Member
from tests.app.endpoints.testcase import EndpointTestCase


class TestCreateCategoryEndpoint(EndpointTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.url = 'v1/category/'
        self.club = self.Club.create()
        self.member = Member.objects.create(
            user=self.client.authorized_user,
            club_id=self.club.id,
            active=True
        )

        self.member.set_admin(True)

    def test_when_body_is_invalid_should_get_bad_request(self):
        body = {
            'name': 'category'
        }
        response = self.client.post(self.get_url(), data=body)
        expected = {'detail': 'Missing required field: club_id', 'status': 400}
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEquals(400, response.status_code)

    def test_when_category_already_exists_should_get_conflict(self):
        body = {
            'name': 'category',
            'club_id': '1'
        }
        Category.objects.create(**body)
        response = self.client.post(self.get_url(), data=body)
        expected = {'detail': 'The category already exists', 'status': 409}
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEquals(409, response.status_code)

    def test_can_create_category_success(self):
        body = {
            'name': 'category',
            'club_id': self.club.id
        }

        response = self.client.post(self.get_url(), data=body)
        expected = Category.objects.get(id=self.club.id).__dto__()
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEqual(201, response.status_code)

    def test_when_club_is_not_found(self):
        body = {
            'name': 'category',
            'club_id': '0'
        }

        response = self.client.post(self.get_url(), data=body)
        expected = {'detail': 'The club does not exists', 'status': 404}
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEquals(404, response.status_code)

    def test_when_user_is_not_admin(self):
        body = {
            'name': 'category',
            'club_id': self.club.id
        }

        self.member.set_admin(False)

        response = self.client.post(self.get_url(), data=body)
        expected = {'detail': 'You must be a admin of the club you are trying to create a category for', 'status': 403}
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEquals(403, response.status_code)
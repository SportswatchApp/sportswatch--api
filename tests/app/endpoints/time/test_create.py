from app.models import Category, Member, Time
from tests.app.endpoints.testcase import EndpointTestCase


class TestCreateTimeEndpoint(EndpointTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.url = 'v1/time/'
        self.trainee = self.Trainee.create()
        self.category = Category.objects.create(
            name='category',
            club=self.trainee.member.club
        )
        self.Member.create(
            user=self.client.authorized_user,
            active=True,
            club=self.trainee.member.club
        )

    def test_when_time_is_missing(self):
        body = {
            'category_id': self.category.id,
            'trainee_id': self.trainee.id,
        }
        response = self.client.post(self.get_url(), data=body)
        expected = {'detail': 'Missing required field: time', 'status': 400}
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEquals(400, response.status_code)

    def test_when_time_is_0(self):
        body = {
            'category_id': self.category.id,
            'trainee_id': self.trainee.id,
            'time': 0
        }
        response = self.client.post(self.get_url(), data=body)
        expected = {'detail': 'Time must be provided as a positive integer in 1/100', 'status': 400}
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEquals(400, response.status_code)

    def test_when_category_not_found(self):
        body = {
            'category_id': 0,
            'trainee_id': self.trainee.id,
            'time': 1700
        }
        response = self.client.post(self.get_url(), data=body)
        expected = {'detail': 'Category not found', 'status': 404}
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEquals(404, response.status_code)

    def test_when_trainee_not_found(self):
        body = {
            'category_id': self.category.id,
            'trainee_id': 0,
            'time': 1700
        }
        response = self.client.post(self.get_url(), data=body)
        expected = {'detail': 'Trainee not found', 'status': 404}
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEquals(404, response.status_code)

    def test_when_user_does_not_have_access_to_register_time_for_trainee(self):
        Member.objects.get(user=self.client.authorized_user).delete()
        body = {
            'category_id': self.category.id,
            'trainee_id': self.trainee.id,
            'time': 1700
        }
        response = self.client.post(self.get_url(), data=body)
        expected = {'detail': 'You do not have permission to register times for this trainee', 'status': 403}
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEquals(403, response.status_code)

    def test_can_post_new_time(self):
        body = {
            'category_id': self.category.id,
            'trainee_id': self.trainee.id,
            'time': 1700
        }
        response = self.client.post(self.get_url(), data=body)
        expected = Time.objects.first().__dto__()
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEquals(201, response.status_code)

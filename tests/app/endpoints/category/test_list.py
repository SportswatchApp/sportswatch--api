from app.models import Member, Trainee, Category
from tests.app.endpoints.testcase import EndpointTestCase

class TestListCategoriesEndpoint(EndpointTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.url = 'v1/trainees/{trainee_id}/categories/'
        self.club = self.Club.create()
        self.member = Member.objects.create(
            user=self.client.authorized_user,
            club_id=self.club.id,
            active=True
        )
        self.trainee = Trainee.objects.create(
            member_id=self.member.id
        )

    def test_when_trainee_is_not_found(self):
        response = self.client.get(self.get_url(path_parameters={'trainee_id': 0}))
        expected = {'detail': 'Trainee not found', 'status': 404}
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEquals(404, response.status_code)

    def test_when_there_are_no_categories(self):
        response = self.client.get(self.get_url(path_parameters={'trainee_id': 1}))
        expected = {'detail': 'No categories found', 'status': 404}
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEquals(404, response.status_code)

    def test_can_list_categories_success(self):
        self.categories = [Category.objects.create(
            name='hej',
            club_id=self.club.id
        ), Category.objects.create(
            name='hej',
            club_id=self.club.id
        )]
        response = self.client.get(self.get_url(path_parameters={'trainee_id': 1}))
        expected = {'detail': 'No categories found', 'status': 200}
        self.assertDictEqual(Category.__dtolist__(self.categories), self.get_response_body(response))
        self.assertEquals(200, response.status_code)

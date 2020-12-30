from app.models import Trainee, Member
from tests.app.endpoints.testcase import EndpointTestCase


class TestApplyMembershipView(EndpointTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.url = 'v1/club/{club_id}/apply/'

    def test_when_club_not_found(self):
        response = self.client.post(self.get_url(path_parameters={'club_id': 0}))
        expected = {'detail': 'Club not found', 'status': 404}
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEquals(404, response.status_code)

    def test_when_application_already_reported(self):
        member = self.Member.create(
            active=False,
            user=self.client.authorized_user
        )
        self.Trainee.create(
            member=member
        )
        response = self.client.post(self.get_url(path_parameters={'club_id': member.club.id}))
        self.assertDictEqual(member.__dto__(), self.get_response_body(response))
        self.assertEquals(208, response.status_code)

    def test_can_create_application(self):
        club = self.Club.create()
        response = self.client.post(self.get_url(path_parameters={'club_id': club.id}))
        expected = Member.objects.get(user=self.client.authorized_user)
        self.assertDictEqual(expected.__dto__(), self.get_response_body(response))
        self.assertEquals(200, response.status_code)

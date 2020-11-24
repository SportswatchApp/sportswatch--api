from app.models import Member
from tests.app.endpoints.testcase import EndpointTestCase


class TestListMembersEndpoint(EndpointTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.url = 'v1/club/{club_id}/members/'

    def test_when_club_not_found(self):
        response = self.client.get(self.get_url(path_parameters={'club_id': 0}))
        expected = {'detail': 'Club not found', 'status': 404}
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEquals(404, response.status_code)

    def test_when_user_does_not_have_permission_for_members(self):
        club = self.Club.create()
        response = self.client.get(self.get_url(path_parameters={'club_id': club.id}))
        expected = {'detail': 'You do not have permission to see these members', 'status': 403}
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEquals(403, response.status_code)

    def test_can_list_members_successfully(self):
        member = self.Member.create(
            user=self.client.authorized_user
        )
        response = self.client.get(self.get_url(path_parameters={'club_id': member.club.id}))
        self.assertDictEqual(Member.__dtolist__([member]), self.get_response_body(response))
        self.assertEquals(200, response.status_code)

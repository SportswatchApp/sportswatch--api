from app.models import Admin, Coach, Member
from tests.app.endpoints.testcase import EndpointTestCase


class TestPutMember(EndpointTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.url = 'v1/club/{club_id}/members/{user_id}/'
        self.user = self.User.create(
            username='dd@dd.com'
        )
        self.member = self.Member.create(
            user=self.client.authorized_user
        )
        self.club = self.member.club

    def test_when_club_not_found_Should_get_not_found(self):
        url = self.get_url(path_parameters={
            'club_id': 0,
            'user_id': self.user.id
        })
        body = {
            'roles': ['trainee']
        }
        response = self.client.put(url, data=body)
        expected = {'detail': 'Club not found', 'status': 404}
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEquals(404, response.status_code)

    def test_when_user_not_found_Should_get_not_found(self):
        url = self.get_url(path_parameters={
            'club_id': self.club.id,
            'user_id': 0
        })
        body = {
            'roles': ['trainee']
        }
        response = self.client.put(url, data=body)
        expected = {'detail': 'User not found', 'status': 404}
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEquals(404, response.status_code)

    def test_when_roles_are_missing_Should_get_bad_request(self):
        url = self.get_url(path_parameters={
            'club_id': self.club.id,
            'user_id': self.user.id
        })
        body = {
            'roles': []
        }
        response = self.client.put(url, data=body)
        expected = {'detail': 'At least one role should be provided', 'status': 400}
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEquals(400, response.status_code)

    def test_when_roles_are_invalid_Should_get_bad_request(self):
        Coach.objects.create(member_id=self.member.id)
        url = self.get_url(path_parameters={
            'club_id': self.club.id,
            'user_id': self.user.id
        })
        body = {
            'roles': ['invalid_role']
        }
        response = self.client.put(url, data=body)
        expected = {'detail': 'Invalid role', 'status': 400}
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEquals(400, response.status_code)

    def test_when_coach_trying_to_add_admin_Should_get_forbidden(self):
        Coach.objects.create(member_id=self.member.id)
        url = self.get_url(path_parameters={
            'club_id': self.club.id,
            'user_id': self.user.id
        })
        body = {
            'roles': ['admin']
        }
        response = self.client.put(url, data=body)
        expected = {'detail': 'Coaches cannot add admins', 'status': 403}
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEquals(403, response.status_code)

    def test_when_trainee_tries_to_add_member_Should_get_forbidden(self):
        url = self.get_url(path_parameters={
            'club_id': self.club.id,
            'user_id': self.user.id
        })
        body = {
            'roles': ['trainee']
        }
        response = self.client.put(url, data=body)
        expected = {'detail': 'Only coaches and admins are allowed to add new members', 'status': 403}
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEquals(403, response.status_code)

    def test_can_put_new_member_success(self):
        Admin.objects.create(member_id=self.member.id)
        url = self.get_url(path_parameters={
            'club_id': self.club.id,
            'user_id': self.user.id
        })
        body = {
            'roles': ['trainee', 'coach']
        }
        response = self.client.put(url, data=body)
        expected = Member.objects.get(user__username='dd@dd.com').__dto__()
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEquals(201, response.status_code)

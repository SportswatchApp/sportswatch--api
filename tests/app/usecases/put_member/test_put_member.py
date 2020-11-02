from parameterized import parameterized

from app.models import User, Club, Member
from app.usecases import put_member
from tests.app.usecases.testcase import UseCaseTestCase


class TestPutMember(UseCaseTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User.objects.create_user(
            username='username',
            password='qwerty'
        )
        self.club = Club.objects.create(name='club')
        self.club_id = self.club.id
        self.user_id = self.user.id
        self.request = self.create_request({
            'roles': ['admin']
        })
        self.request_user = User.objects.create_user(
            username='request user',
            password='qwerty'
        )
        self.request_user_member = Member.objects.create(
            user=self.request_user,
            club=self.club,
            active=True
        )
        self.request.user = self.request_user

    def test_when_roles_not_in_request(self):
        self.request = self.create_request({})
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_invalid_request)

    def test_when_roles_list_is_empty(self):
        self.request = self.create_request({
            'roles': []
        })
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_invalid_request)

    def test_when_club_does_not_exist(self):
        self.club_id = 0
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_club_not_found)

    def test_when_user_does_not_exist(self):
        self.user_id = 0
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_user_not_found)

    def test_when_user_not_member_of_club_Should_deny(self):
        member = Member.objects.create(
            club=Club.objects.create(name='other'),
            user=self.user,
            active=True
        )
        member.set_coach(True)
        member.set_trainee(True)
        member.set_admin(True)
        self.request.user = self.user
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_forbidden)

    def test_when_coach_trying_to_put_admin_Should_deny(self):
        self.request_user_member.set_coach(True)
        self.request_user_member.set_admin(False)
        self.request = self.create_request({
            'roles': ['admin']
        })
        self.request.user = self.request_user
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_forbidden_coach_action)

    @parameterized.expand([
        [True, True, ['admin', 'coach', 'trainee']],
        [True, False, ['admin', 'coach', 'trainee']],
        [False, True, ['coach', 'trainee']]
    ])
    def test_different_member_types_of_success(self, is_admin, is_coach, roles):
        self.request_user_member.set_admin(is_admin)
        self.request_user_member.set_coach(is_coach)
        self.request = self.create_request({
            'roles': roles
        })
        self.request.user = self.request_user
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_success)
        actual_member = Member.objects.exclude(pk=self.request_user_member.pk).first()
        self.assertEqualRoles(actual_member, roles)
        self.assertFalse(actual_member.active)
        self.assertEqual(self.request_user, actual_member.invited_by)

    @parameterized.expand([
        [True, True, ['admin', 'coach', 'trainee']],
        [True, False, ['admin', 'coach', 'trainee']],
        [False, True, ['coach', 'trainee']],
        [True, True, ['trainee']],
        [True, True, ['coach']]
    ])
    def test_when_user_already_member_Should_update_roles(self, is_admin, is_coach, roles):
        self.request_user_member.set_admin(is_admin)
        self.request_user_member.set_coach(is_coach)
        self.request = self.create_request({
            'roles': roles
        })
        self.request.user = self.request_user
        member = Member.objects.create(
            club=self.club,
            user=self.user,
            active=True,
            invited_by=self.request_user
        )
        member.set_trainee(True)
        member.set_coach(True)
        member.set_admin(True)
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_success)
        actual_member = Member.objects.get(pk=member.id)
        self.assertEqualRoles(actual_member, roles)
        self.assertTrue(actual_member.active)
        self.assertEqual(self.request_user, actual_member.invited_by)

    def assertEqualRoles(self, member, roles):
        if 'admin' in roles:
            self.assertTrue(member.is_admin())
        else:
            self.assertFalse(member.is_admin())

        if 'coach' in roles:
            self.assertTrue(member.is_coach())
        else:
            self.assertFalse(member.is_coach())

        if 'trainee' in roles:
            self.assertTrue(member.is_trainee())
        else:
            self.assertFalse(member.is_trainee())


    def create_request(self, fields):
        return put_member.Request().from_dict(fields)

    def run_use_case(self):
        put_member.Put.put(self.club_id, self.user_id, self.request, self.listener)

from unittest import mock
from unittest.mock import Mock
from django.db import IntegrityError
from app.models import Trainee, Member
from app.usecases import apply_membership
from tests.app.usecases.testcase import UseCaseTestCase


class TestApplyMembershipUseCase(UseCaseTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = self.User.create()

    def test_when_club_id_not_found(self):
        self.request = self.create_request({
            'club_id': 0
        })
        self.request.user = self.user
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_not_found)

    def test_when_user_already_member_of_club(self):
        member = self.Member.create()
        self.request = self.create_request({
            'club_id': member.club.id
        })
        self.request.user = member.user
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_already_applied)

    def test_when_database_error(self):
        self.request = self.create_request({
            'club_id': self.Club.create().id
        })
        self.request.user = self.user
        with mock.patch.object(Trainee.objects, 'create') as e:
            e.side_effect = Mock(side_effect=IntegrityError())
            self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_database_error)

    def test_can_apply_Success(self):
        self.request = self.create_request({
            'club_id': self.Club.create().id
        })
        self.request.user = self.user
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_success)
        actual = self.get_query_set()
        expected = Member.objects.first()
        self.assertEquals(expected.__dto__(), actual)

    def run_use_case(self):
        apply_membership.Apply.apply(self.request, self.listener)

    def create_request(self, fields):
        return apply_membership.Request().from_dict(fields)

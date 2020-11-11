from django.test import TestCase

from app.models import Club, Member, User, Admin
from tests.object_environment.factory import EnvironmentFactory


class TestUser(TestCase, EnvironmentFactory):

    def setUp(self) -> None:
        self.club = Club.objects.create(name='club')

    def test_member_of_True(self):
        user = User.objects.create_user(
            username='username',
            password='qwerty'
        )
        member = Member.objects.create(
            club=self.club,
            user=user,
            active=True,
        )
        Admin.objects.create(
            member=member
        )
        self.assertTrue(user.admin_of(self.club))

    def test_member_of_False(self):
        user = User.objects.create_user(
            username='username',
            password='qwerty'
        )
        Member.objects.create(
            club=self.club,
            user=user,
            active=True,
        )
        self.assertFalse(user.admin_of(self.club))

    def test_can_register_for_trainee_of_own_club(self):
        club = self.Club.create()
        user = self.User.create()
        self.Member.create(
            club_id=club.id,
            user_id=user.id
        )
        trainee = self.Trainee.create(
            club=club
        )
        self.assertTrue(user.can_register_for(trainee))

    def test_can_register_for_trainee_where_user_is_trusted(self):
        club = self.Club.create()
        user = self.User.create()
        self.Member.create(
            club_id=club.id,
            user_id=user.id
        )
        trainee = self.Trainee.create()
        trainee.member.club.trusted_users.add(user)
        self.assertTrue(user.can_register_for(trainee))

    def test_cannot_register_for_trainee_where_user_not_trusted_nor_member(self):
        club = self.Club.create()
        user = self.User.create()
        self.Member.create(
            club_id=club.id,
            user_id=user.id
        )
        trainee = self.Trainee.create()
        self.assertFalse(user.can_register_for(trainee))

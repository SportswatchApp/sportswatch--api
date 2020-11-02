from django.test import TestCase

from app.models import Club, Member, User, Admin


class TestUser(TestCase):

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

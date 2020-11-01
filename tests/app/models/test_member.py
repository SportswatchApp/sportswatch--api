from django.test import TestCase

from app.models import Club, Member, User, Coach, Admin, Trainee


class TestMember(TestCase):

    def setUp(self) -> None:
        club = Club.objects.create(name='club')
        user = User.objects.create_user(username='user', password='qwerty')
        self.member = Member.objects.create(
            club=club,
            user=user
        )

    def test_set_coach_True(self):
        self.assertEqual(0, Coach.objects.count())
        self.member.set_coach(True)
        self.assertEqual(1, Coach.objects.count())
        self.assertTrue(self.member.is_coach())
        self.member.set_coach(True)
        self.assertEqual(1, Coach.objects.count())
        self.assertTrue(self.member.is_coach())

    def test_set_admin_True(self):
        self.assertEqual(0, Admin.objects.count())
        self.member.set_admin(True)
        self.assertEqual(1, Admin.objects.count())
        self.assertTrue(self.member.is_admin())
        self.member.set_admin(True)
        self.assertEqual(1, Admin.objects.count())
        self.assertTrue(self.member.is_admin())

    def test_set_trainee_True(self):
        self.assertEqual(0, Trainee.objects.count())
        self.member.set_trainee(True)
        self.assertEqual(1, Trainee.objects.count())
        self.assertTrue(self.member.is_trainee())
        self.member.set_trainee(True)
        self.assertEqual(1, Trainee.objects.count())
        self.assertTrue(self.member.is_trainee())

    def test_set_coach_False(self):
        self.member.set_coach(True)
        self.assertEqual(1, Coach.objects.count())
        self.member.set_coach(False)
        self.assertEqual(0, Coach.objects.count())

    def test_set_admin_False(self):
        self.member.set_admin(True)
        self.assertEqual(1, Admin.objects.count())
        self.member.set_admin(False)
        self.assertEqual(0, Admin.objects.count())

    def test_set_trainee_False(self):
        self.member.set_trainee(True)
        self.assertEqual(1, Trainee.objects.count())
        self.member.set_trainee(False)
        self.assertEqual(0, Trainee.objects.count())

from app.models import Club, Member, Admin, User
from app.usecases import create_club
from tests.app.usecases.testcase import UseCaseTestCase


class TestCreateClub(UseCaseTestCase):

    def setUp(self) -> None:
        super().setUp()

    def test_when_request_is_invalid(self):
        self.request = self.create_request({
            'name': ''
        })
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_invalid_request)
        self.assertEqual(0, Club.objects.count())
        self.assertEqual(0, Member.objects.count())
        self.assertEqual(0, Admin.objects.count())

    def test_can_create_club(self):
        self.request = self.create_request({
            'name': 'Club'
        })
        self.request.user = User.objects.create_user(
            username='user',
            password='qwerty'
        )
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_success)
        club = Club.objects.first()
        self.assertEqual('Club', club.name)
        member = club.member_set.first()
        self.assertTrue(member.is_admin())
        self.assertEqual(self.request.user, member.user)

    def create_request(self, fields):
        return create_club.Request().from_dict(fields)

    def run_use_case(self):
        create_club.Create.create(self.request, self.listener)

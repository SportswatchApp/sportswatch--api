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
            'name': 'Club',
            'region': 'North',
            'country': 'Denmark',
            'zip_code': '9000',
            'city': 'Aalborg'
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
        self.assertTrue(member.active)
        self.assertEqual(self.request.user, member.user)
        self.assertTrue(club.has_active_member(member.user))

    def test_when_club_already_exist(self):
        data = {
            'name': 'Club',
            'region': 'North',
            'country': 'Denmark',
            'zip_code': '9000',
            'city': 'Aalborg'
        }
        Club.objects.create(**data)  # Existing club
        self.request = self.create_request(data)
        self.request.user = User.objects.create_user(
            username='user',
            password='qwerty'
        )
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_already_exist)

    def create_request(self, fields):
        return create_club.Request().from_dict(fields)

    def run_use_case(self):
        create_club.Create.create(self.request, self.listener)

from abc import ABC

from app.models import Club, Category, User, Member
from app.usecases import create_category
from tests.app.usecases.testcase import UseCaseTestCase


class TestCreateCategory(UseCaseTestCase):

    def setUp(self) -> None:
        super().setUp()

    def test_when_request_is_invalid(self):
        self.request = self.create_request({
         'name': 'category',
        })
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_invalid_request)
        self.assertEqual(0, Category.objects.count())

    def test_can_create_category(self):
        club = Club.objects.create(**{
            'name': 'Club',
            'region': 'North',
            'country': 'Denmark',
            'zip_code': '9000',
            'city': 'Aalborg'
        })

        self.request = self.create_request({
            'name': 'category',
            'club_id': 1
        })

        self.request.user = User.objects.create_user(
            username='user',
            password='qwerty'
        )

        Member.objects.create(
            user=self.request.user,
            club=club
        )

        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_success)
        category = Category.objects.first()
        self.assertEqual('category', category.name)
        club = Club.objects.first()
        self.assertEqual(1, club.id)

    def test_when_category_already_exists(self):
        club = Club.objects.create(**{
            'name': 'Club',
            'region': 'North',
            'country': 'Denmark',
            'zip_code': '9000',
            'city': 'Aalborg'
        })
        data = {
            'name': 'category',
            'club_id': 1
        }

        Category.objects.create(**data)
        self.request = self.create_request(data)

        self.request.user = User.objects.create_user(
            username='user',
            password='qwerty'
        )
        Member.objects.create(
            user=self.request.user,
            club=club
        )

        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_already_exist)

    def test_when_club_does_not_exist(self):
        self.request = self.create_request({
            'name': 'category',
            'club_id': 1
        })
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_club_does_not_exist)

    def test_when_user_is_not_a_member(self):
        club = Club.objects.create(**{
            'name': 'Club',
            'region': 'North',
            'country': 'Denmark',
            'zip_code': '9000',
            'city': 'Aalborg'
        })

        self.request = self.create_request({
            'name': 'category',
            'club_id': 1
        })

        self.request.user = User.objects.create_user(
            username='user',
            password='qwerty'
        )

        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_user_must_be_member_of_club)

    def create_request(self, fields):
        return create_category.Request().from_dict(fields)

    def run_use_case(self):
        create_category.Create.create(self.request, self.listener)

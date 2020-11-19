from unittest import mock
from unittest.mock import Mock

from django.db import IntegrityError
from app.models import Category, User, Time
from app.usecases import create_time
from tests.app.usecases.testcase import UseCaseTestCase


class TestCreateTime(UseCaseTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.club = self.Club.create()
        self.trainee = self.Trainee.create(club=self.club)
        self.category = Category.objects.create(
            name='category',
            club_id=self.club.id
        )
        self.reported_by = self.User.create()

    def test_when_request_is_in_valid(self):
        self.request = self.create_request({
            'time': ''
        })
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_invalid_request)

    def test_when_trainee_not_found(self):
        self.request = self.create_request({
            'time': 100,
            'trainee_id': 0,
        })
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_trainee_not_found)

    def test_when_user_cannot_report_times_for_trainee(self):
        self.request = self.create_request({})
        self.request.user = self.User.create()
        with mock.patch.object(User, 'can_register_for') as m:
            m.return_value = False
            self.run_use_case()
            self.assertOnlyCalled(self.listener.handle_forbidden)

    def test_when_category_not_in_club(self):
        category = Category.objects.create(
            name='Category2',
            club=self.Club.create()
        )
        self.request = self.create_request({
            'category_id': category.id
        })
        user = self.Trainee.create(club=self.club).member.user
        self.request.user = user
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_illegal_category)

    def test_when_database_error(self):
        self.request = self.create_request({})
        user = self.Trainee.create(club=self.club).member.user
        self.request.user = user
        with mock.patch.object(Time.objects, 'create') as e:
            e.side_effect = Mock(side_effect=IntegrityError)
            self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_database_error)

    def test_can_create_new_time_Success(self):
        self.request = self.create_request({})
        user = self.Trainee.create(club=self.club).member.user
        self.request.user = user
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_success)
        actual = self.get_query_set()
        expected = Time.objects.first()
        self.assertEqual(expected.__dto__(), actual)

    def create_request(self, fields):
        return create_time.Request().from_dict(
            {**{
                'time': 100,
                'trainee_id': self.trainee.id,
                'category_id': self.category.id
            }, **fields}
        )

    def run_use_case(self):
        create_time.Create.create(self.request, self.listener)

from abc import ABC

from app.models import Club, User, Member, Trainee, Category
from tests.app.usecases.testcase import UseCaseTestCase
from app.usecases import list_categories

class TestListCategories(UseCaseTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.trainee_id = 0
        self.user = User.objects.create_user(
            username='username',
            password='qwerty'
        )
        self.club = Club.objects.create(name='club')
        self.member = Member.objects.create(
            club=self.club,
            user=self.user,
            active=False
        )

    def test_can_list_categories(self):
        trainee = Trainee.objects.create(member=self.member)
        self.trainee_id = trainee.id
        Category.objects.create(club_id=self.club.id)
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_success)

    def test_when_trainee_does_not_exist(self):
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_not_found)

    def test_when_there_is_no_categories(self):
        trainee = Trainee.objects.create(member=self.member)
        self.trainee_id = trainee.id
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_no_categories)

    def run_use_case(self):
        list_categories.List.list(self.listener, self.trainee_id)

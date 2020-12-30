from parameterized import parameterized
from app.usecases import get_times
from tests.app.usecases.testcase import UseCaseTestCase


class TestGetTimesUseCase(UseCaseTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = self.User.create()

    def test_when_trainee_not_found(self):
        self.request = self.create_request({
            'trainee_id': 0
        })
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_not_found)

    def test_when_trainee_and_user_is_the_same_Should_get_success(self):
        member = self.Member.create(user=self.user)
        trainee = self.Trainee.create(member=member)
        self.request = self.create_request({
            'trainee_id': trainee.id
        })
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_success)

    def test_when_user_is_trusted_user_by_trainee_Should_get_success(self):
        trainee = self.Trainee.create()
        trainee.member.club.trusted_users.add(self.user)
        self.request = self.create_request({
            'trainee_id': trainee.id
        })
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_success)

    @parameterized.expand([
        [True],
        [False]
    ])
    def test_when_user_is_coach_or_admin_of_club_Should_get_success(self, coach):
        member = self.Member.create(user=self.user)
        if coach:
            member.set_coach(True)
        else:
            member.set_admin(True)

        trainee = self.Trainee.create(member=self.Member.create(club=member.club))
        self.request = self.create_request({
            'trainee_id': trainee.id
        })
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_success)

    def test_when_user_is_not_coach_nor_admin_nor_trusted_Should_get_forbidden(self):
        member = self.Member.create(user=self.user)
        trainee = self.Trainee.create(member=self.Member.create(club=member.club))
        self.assertEqual(member.club, trainee.member.club)
        self.request = self.create_request({
            'trainee_id': trainee.id
        })
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_forbidden)

    def test_when_user_is_not_member_of_club_nor_trusted_Should_get_forbidden(self):
        trainee = self.Trainee.create()
        self.request = self.create_request({
            'trainee_id': trainee.id
        })
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_forbidden)

    def create_request(self, fields):
        request = get_times.Request().from_dict(fields)
        request.user = self.user
        return request

    def run_use_case(self):
        get_times.Get.get(self.request, self.listener)

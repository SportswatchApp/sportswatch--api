from app.models import User, Club, Member
from app.usecases import get_members
from tests.app.usecases.testcase import UseCaseTestCase


class TestGetMembers(UseCaseTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.club_id = 0
        self.user = User.objects.create_user(
            username='username',
            password='qwerty'
        )

    def test_when_club_not_found(self):
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_not_found)

    def test_when_user_does_not_have_permission(self):
        club = Club.objects.create(name='club')
        self.club_id = club.id
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_forbidden)

    def test_when_user_is_inactive_member_Cannot_get(self):
        club = Club.objects.create(name='club')
        self.club_id = club.id
        Member.objects.create(
            club=club,
            user=self.user,
            active=False
        )
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_forbidden)

    def test_when_user_is_active_member_Can_get_members(self):
        club = Club.objects.create(name='club')
        self.club_id = club.id
        Member.objects.create(
            club=club,
            user=self.user,
            active=True
        )
        self.run_use_case()
        self.assertOnlyCalled(self.listener.handle_success)

    def create_request(self, fields):
        return super().create_request(fields)

    def run_use_case(self):
        get_members.Get.get(self.club_id, self.user, self.listener)

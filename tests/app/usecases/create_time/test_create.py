from app.models import Category
from app.usecases import create_time
from tests.app.usecases.testcase import UseCaseTestCase


class TestCreateTime(UseCaseTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.trainee = self.Trainee.create()
        self.category = Category.objects.create(
            name=''
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

    def create_request(self, fields):
        return create_time.Request().from_dict(fields)

    def run_use_case(self):
        create_time.Create.create(self.request, self.listener)

from app.models import Trainee
from tests.app.endpoints.testcase import EndpointTestCase


class TestListTraineesEndpoint(EndpointTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.url = 'v1/trainees/'
        member = self.Member.create(
            user=self.client.authorized_user
        )
        self.trainees = [
            self.Trainee.create(club=member.club),
            self.Trainee.create(club=member.club)
        ]

    def test_can_get_trainees(self):
        response = self.client.get(self.get_url())
        expected = Trainee.__dtolist__(self.trainees)
        actual = self.get_response_body(response)
        self.assertDictEqual(expected, actual)
        self.assertEquals(200, response.status_code)

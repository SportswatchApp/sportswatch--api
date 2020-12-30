from app.models import Time
from tests.app.endpoints.testcase import EndpointTestCase


class TestListTraineeTimesEndpoint(EndpointTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.url = 'v1/trainees/{id}/times/'

    def test_when_trainee_not_found_Should_get_not_found(self):
        response = self.client.get(self.get_url(path_parameters={'id': 0}))
        expected = {"detail": "Trainee not found", "status": 404}
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEqual(404, response.status_code)

    def test_forbidden(self):
        trainee = self.Trainee.create()
        response = self.client.get(self.get_url(path_parameters={'id': trainee.id}))
        expected = {"detail": "You do not have access to list times for this trainee", "status": 403}
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEqual(403, response.status_code)

    def test_success(self):
        member = self.Member.create(user=self.client.authorized_user)
        member.set_coach(True)
        trainee = self.Trainee.create(
            member=self.Member.create(club=member.club)
        )
        [self.Time.create(trainee=trainee) for _ in range(2)]
        response = self.client.get(self.get_url(path_parameters={'id': trainee.id}))
        expected = Time.__dtolist__(Time.objects.all())
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEqual(200, response.status_code)

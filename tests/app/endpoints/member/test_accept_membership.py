from tests.app.endpoints.testcase import EndpointTestCase


class TestAcceptMembershipEndpoint(EndpointTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.url = 'v1/members/{member_id}/accept/'

    def test_when_member_not_found(self):
        url = self.get_url(path_parameters={
            'member_id': 0
        })
        response = self.client.put(url)
        expected = {'detail': 'Member not found', 'status': 404}
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEquals(404, response.status_code)

    def test_when_forbidden_accept(self):
        member = self.Member.create()
        url = self.get_url(path_parameters={
            'member_id': member.id
        })
        response = self.client.put(url)
        expected = {'detail': 'You do not have permission to do this', 'status': 403}
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEquals(403, response.status_code)

    def test_can_accept_membership(self):
        member = self.Member.create(user=self.client.authorized_user)
        url = self.get_url(path_parameters={
            'member_id': member.id
        })
        response = self.client.put(url)
        expected = {'detail': 'Membership accepted'}
        self.assertDictEqual(expected, self.get_response_body(response))
        self.assertEquals(202, response.status_code)

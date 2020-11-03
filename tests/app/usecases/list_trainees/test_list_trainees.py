import random

from parameterized import parameterized

from app.models import Time, Category, Trainee
from app.usecases import list_trainees
from tests.app.usecases.testcase import UseCaseTestCase


class TestListTrainees(UseCaseTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.member = self.Member.create()
        self.user = self.member.user
        # Noise
        self.Trainee.create()
        self.Trainee.create()
        self.Trainee.create()

    def test_can_get_trainees_from_same_club(self):
        trainees = self._create_trainees(self.member.club, 4)
        self.request = self.create_request({
            'order_by': '',
            'q': ''
        })
        self.run_use_case()
        actual = self.get_query_set()
        self.assertCountEqual(Trainee.__dtolist__(trainees), actual)

    def test_can_get_trainees_from_same_clubs(self):
        new_member = self.Member.create(user_id=self.user.id)
        self.assertEqual(2, len(self.user.clubs()))
        trainees_club1 = self._create_trainees(self.member.club, 2)
        trainees_club2 = self._create_trainees(new_member.club, 3)
        trainees_club1_and_club2 = self._create_trainees_two_clubs(
            club1=self.member.club,
            club2=new_member.club,
            amt=2
        )
        trainees = set(trainees_club1 + trainees_club2 + trainees_club1_and_club2)
        self.assertEqual(7, len(trainees))
        self.request = self.create_request({
            'order_by': '',
            'q': ''
        })
        self.run_use_case()
        actual = self.get_query_set()
        self.assertCountEqual(Trainee.__dtolist__(trainees), actual)

    def test_can_get_trainees_where_user_is_trusted(self):
        club = self.Club.create()
        club.trusted_users.add(self.user)
        self.assertNotIn(club, self.user.clubs())
        trainees = self._create_trainees(club, 3)
        self.request = self.create_request({
            'order_by': '',
            'q': ''
        })
        self.run_use_case()
        actual = self.get_query_set()
        self.assertCountEqual(Trainee.__dtolist__(trainees), actual)

    def test_can_get_trainees_from_multiple_clubs_where_user_is_trusted(self):
        club1 = self.Club.create()
        club2 = self.Club.create()
        club1.trusted_users.add(self.user)
        club2.trusted_users.add(self.user)

        self.assertNotIn(club1, self.user.clubs())
        self.assertNotIn(club2, self.user.clubs())

        trainees_club_1 = self._create_trainees(club1, 3)
        trainees_club_2 = self._create_trainees(club2, 3)
        trainees = set(trainees_club_1 + trainees_club_2)

        self.request = self.create_request({
            'order_by': '',
            'q': ''
        })
        self.run_use_case()
        actual = self.get_query_set()
        self.assertCountEqual(Trainee.__dtolist__(trainees), actual)

    @parameterized.expand([
        ['John', 'Doe', 'johnd'],
    ])
    def test_can_search_by_full_name_inside_trainees(self, first_name, last_name, search_string):
        trainees = self._create_trainees(self.member.club, 4)
        trainee = self.Trainee.create()
        trainee.member.club = self.member.club
        trainee.member.save()
        trainee.member.user.first_name = first_name
        trainee.member.user.last_name = last_name
        trainee.member.user.save()
        trainees.append(trainee)
        self.request = self.create_request({
            'order_by': '',
            'q': search_string
        })
        self.run_use_case()
        actual = self.get_query_set()
        self.assertCountEqual([trainee.__dto__()], actual)

    def test_can_search_by_email_inside_trainees(self):
        trainees = self._create_trainees(self.member.club, 4)
        trainee = self.Trainee.create()
        trainee.member.club = self.member.club
        trainee.member.save()
        trainee.member.user.username = 'christian@doe.com'
        trainee.member.user.save()
        trainees.append(trainee)
        self.request = self.create_request({
            'order_by': '',
            'q': 'christian@do'
        })
        self.run_use_case()
        actual = self.get_query_set()
        self.assertCountEqual([trainee.__dto__()], actual)

    def test_can_search_by_exact_id_inside_trainees(self):
        trainees = self._create_trainees(self.member.club, 4)
        trainee = self.Trainee.create()
        trainee.member.club = self.member.club
        trainee.member.user = self.User.create(pk=8934)
        trainee.member.save()
        trainees.append(trainee)
        self.request = self.create_request({
            'order_by': '',
            'q': '8934'
        })
        self.run_use_case()
        actual = self.get_query_set()
        self.assertCountEqual([trainee.__dto__()], actual)

    def test_can_order_by_num_registrations(self):
        trainees = self._create_trainees_with_times(5)
        random.shuffle(trainees)
        self.request = self.create_request({
            'order_by': 'frequently',
            'q': ''
        })
        self.run_use_case()
        actual = self.get_query_set()
        trainees.sort(reverse=False, key=lambda t: t.time_set.count())
        self.assertEqual(Trainee.__dtolist__(trainees), list(actual))

    def create_request(self, fields):
        request = list_trainees.Request().from_dict(fields)
        request.user = self.user
        return request

    def run_use_case(self):
        list_trainees.List.list(self.request, self.listener)

    def get_query_set(self):
        return self.listener.handle_success.call_args[0][0]

    def _create_trainees(self, club, amt):
        return [self.Trainee.create(club=club) for i in range(amt)]

    def _create_trainees_two_clubs(self, club1, club2, amt):
        trainees = self._create_trainees(club1, amt)
        for t in trainees:
            self.Member.create(club=club2, user=t.member.user)
            self.assertEqual(2, len(t.member.user.clubs()))

        return trainees

    def _create_trainees_with_times(self, amt):
        cat = Category.objects.create(name='c')
        trainees = []
        for i in range(amt):
            trainee = self.Trainee.create(club=self.member.club)
            for j in range(i):
                Time.objects.create(
                    time=10,
                    category=cat,
                    reported_by=self.user,
                    trainee=trainee
                )
                Time.objects.create(
                    time=3,
                    category=cat,
                    reported_by=self.User.create(),
                    trainee=trainee
                )
            trainees.append(trainee)
        return trainees

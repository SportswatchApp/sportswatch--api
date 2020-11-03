from app.models import Trainee
from tests.object_environment.environment import ObjectEnvironment
from tests.object_environment.environments.member import MemberEnvironment


class TraineeEnvironment(ObjectEnvironment):

    def create(self, **kwargs):
        self.club = kwargs.pop('club', None)
        update = self.provider.kwargs(self._default(), kwargs)
        trainee = Trainee(**update)
        self._create_references_if_missing(trainee)
        trainee.save()
        return trainee

    def _default(self):
        return {}

    def _create_references_if_missing(self, obj):
        if not obj.member_id:
            if self.club:
                obj.member = MemberEnvironment(self.provider).create(club=self.club)
            else:
                obj.member = MemberEnvironment(self.provider).create()

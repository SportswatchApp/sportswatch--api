from app.models import Category, Time
from tests.object_environment.environment import ObjectEnvironment
from tests.object_environment.environments.trainee import TraineeEnvironment
from tests.object_environment.environments.user import UserEnvironment


class TimeEnvironment(ObjectEnvironment):

    def create(self, **kwargs):
        update = self.provider.kwargs(self._default(), kwargs)
        time = Time(**update)
        self._create_references_if_missing(time)
        time.save()
        return time

    def _default(self):
        return {
            'time': self.provider.unique_number(),
        }

    def _create_references_if_missing(self, obj):
        if not obj.trainee_id:
            obj.trainee = TraineeEnvironment(self.provider).create()
        if not obj.category_id:
            obj.category = Category.objects.create(
                club=obj.trainee.member.club
            )
        if not obj.reported_by_id:
            obj.reported_by = UserEnvironment(self.provider).create()

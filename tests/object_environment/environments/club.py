from app.models import Club
from tests.object_environment.environment import ObjectEnvironment


class ClubEnvironment(ObjectEnvironment):

    def create(self, **kwargs):
        update = self.provider.kwargs(self._default(), kwargs)
        club = Club(**update)
        club.save()
        return club

    def _default(self):
        return {
            'name': self.provider.unique_text(max_length=20),
            'region': self.provider.unique_text(max_length=30),
            'zip_code': self.provider.unique_text(max_length=10),
            'city': self.provider.unique_text(max_length=35),
            'country': self.provider.unique_text(max_length=35)
        }

    def _create_references_if_missing(self, obj):
        pass

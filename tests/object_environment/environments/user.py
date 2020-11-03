from app.models import User
from tests.object_environment.environment import ObjectEnvironment


class UserEnvironment(ObjectEnvironment):

    def create(self, **kwargs):
        update = self.provider.kwargs(self._default(), kwargs)
        user = User(**update)
        user.save()
        return user

    def _default(self):
        return {
            'username': self.provider.unique_text(),
            'password': self.provider.unique_text(),
            'is_staff': False,
            'is_superuser': False,
            'is_active': True
        }

    def _create_references_if_missing(self, obj):
        pass

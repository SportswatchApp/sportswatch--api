from app.models import Member
from tests.object_environment.environment import ObjectEnvironment
from tests.object_environment.environments.club import ClubEnvironment
from tests.object_environment.environments.user import UserEnvironment


class MemberEnvironment(ObjectEnvironment):

    def create(self, **kwargs):
        update = self.provider.kwargs(self._default(), kwargs)
        member = Member(**update)
        self._create_references_if_missing(member)
        member.save()
        return member

    def _default(self):
        return {
            'active': True,
            'marked_spam': False,
            'invited_by': None
        }

    def _create_references_if_missing(self, obj):
        if not obj.club_id:
            obj.club = ClubEnvironment(self.provider).create()

        if not obj.user_id:
            obj.user = UserEnvironment(self.provider).create()

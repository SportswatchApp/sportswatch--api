from collections import namedtuple

from django.contrib.auth.models import AbstractUser

from .member import Member


class User(AbstractUser):
    pass

    DTO = namedtuple('DTO', 'id email first_name last_name date_joined')

    def admin_of(self, club):
        try:
            member = club.member_set.get(
                user=self,
                active=True,
            )
            return member.is_admin()
        except Member.DoesNotExist:
            return False

    def coach_of(self, club):
        try:
            member = club.member_set.get(
                user=self,
                active=True,
            )
            return member.is_coach()
        except Member.DoesNotExist:
            return False

    def __dto__(self):
        return User.DTO(
            id=self.id,
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
            date_joined=self.date_joined
        )._asdict()

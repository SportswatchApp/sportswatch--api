from collections import namedtuple

from django.contrib.auth.models import AbstractUser

from .member import Member


class User(AbstractUser):
    pass

    DTO = namedtuple('DTO', 'id email first_name last_name date_joined members')

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

    def clubs(self):
        return {m.club for m in self.member_set.all()}

    def can_register_for(self, trainee):
        clubs = self.clubs()
        if trainee.member.club in clubs:
            return True
        elif trainee.member.club.trusted_users.filter(pk=self.pk).exists():
            return True
        else:
            return False

    def members(self, only_active=True):
        if only_active:
            return self.member_set.filter(active=True)
        else:
            return self.member_set.all()

    def is_member_of(self, club):
        if isinstance(club, int):
            return self.member_set.filter(club_id=club).exists()
        else:
            return self.member_set.filter(club=club).exists()

    def __dto__(self):
        return User.DTO(
            id=self.id,
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
            date_joined=self.date_joined,
            members=[m.__dto_no_user__() for m in self.members()]
        )._asdict()

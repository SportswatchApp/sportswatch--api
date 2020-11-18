from collections import namedtuple
from .coach import Coach
from .admin import Admin
from .trainee import Trainee
from django.db import models


class Member(models.Model):
    user = models.ForeignKey(
        to='app.User',
        on_delete=models.CASCADE,
        verbose_name='Bruger'
    )
    club = models.ForeignKey(
        to='app.Club',
        on_delete=models.CASCADE,
        verbose_name='Klub'
    )
    active = models.BooleanField(
        default=False
    )
    marked_spam = models.BooleanField(
        default=False
    )
    invited_by = models.ForeignKey(
        to='app.User',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Inviteret af',
        related_name='invited_by'
    )
    date_joined = models.DateTimeField(
        auto_now_add=True
    )

    DTO = namedtuple("DTO", "id club date_joined user is_trainee is_coach is_admin active links")
    ROLES = ['admin', 'coach', 'trainee']

    def is_trainee(self):
        return self.trainee_set.exists()

    def is_coach(self):
        return self.coach_set.exists()

    def is_admin(self):
        return self.admin_set.exists()

    def is_pending(self):
        return self.active is False and self.marked_spam is False

    def set_admin(self, set_admin):
        if set_admin:
            Admin.objects.get_or_create(member=self)
        else:
            Admin.objects.filter(member=self).delete()

    def set_coach(self, set_coach):
        if set_coach:
            Coach.objects.get_or_create(member=self)
        else:
            Coach.objects.filter(member=self).delete()

    def set_trainee(self, set_trainee):
        if set_trainee:
            Trainee.objects.get_or_create(member=self)
        else:
            Trainee.objects.filter(member=self).delete()

    def __dto__(self):
        return Member.DTO(
            id=self.id,
            club={
                'id': self.club_id,
                'name': self.club.name
            },
            date_joined=self.date_joined,
            user=self.user.__dto__(),
            is_trainee=self.is_trainee(),
            is_coach=self.is_coach(),
            is_admin=self.is_admin(),
            active=self.active,
            links={
                'club': '/api/v1/club/' + str(self.club_id) + '/'
            }
        )._asdict()

    def __dto_no_user__(self):
        return Member.DTO(
            id=self.id,
            club={
                'id': self.club_id,
                'name': self.club.name
            },
            date_joined=self.date_joined,
            user={'id': self.user.id},
            is_trainee=self.is_trainee(),
            is_coach=self.is_coach(),
            is_admin=self.is_admin(),
            active=self.active,
            links={
                'club': '/api/v1/club/' + str(self.club_id) + '/'
            }
        )._asdict()

    @staticmethod
    def __dtolist__(members):
        return [m.__dto__() for m in members]

    class Meta:
        unique_together = ('user', 'club',)

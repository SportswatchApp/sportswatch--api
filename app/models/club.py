from collections import namedtuple

from django.db import models


class Club(models.Model):
    name = models.CharField(
        max_length=120,
        verbose_name='Navn'
    )
    created_date = models.DateTimeField(auto_now_add=True)

    DTO = namedtuple("DTO", "id name created_date members")

    def has_member(self, user):
        return self.member_set.filter(user=user).exists()

    def __dto__(self):
        return Club.DTO(
            id=self.id,
            name=self.name,
            created_date=self.created_date,
            members={'link': '/api/v1/club/' + str(self.id) + '/members/'}
        )._asdict()

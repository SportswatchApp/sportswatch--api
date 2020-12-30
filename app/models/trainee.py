from collections import namedtuple

from django.db import models


class Trainee(models.Model):
    member = models.ForeignKey(
        to='app.Member',
        on_delete=models.CASCADE,
        verbose_name='Medlem'
    )

    DTO = namedtuple('DTO', 'id member links')

    @staticmethod
    def __dtolist__(trainees):
        return {'trainees': [t.__dto__() for t in trainees]}

    def __dto__(self):
        return Trainee.DTO(
            id=self.id,
            member=self.member.__dto__(),
            links={}
        )._asdict()

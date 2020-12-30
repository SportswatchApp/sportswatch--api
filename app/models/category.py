from collections import namedtuple

from django.db import models
from .club import Club


class Category(models.Model):
    name = models.CharField(
        max_length=45,
        verbose_name='Navn'
    )
    club = models.ForeignKey(
        to=Club,
        on_delete=models.CASCADE
    )

    DTO = namedtuple('DTO', 'name club')

    def __dto__(self):
        return Category.DTO(
            name=self.name,
            club=self.club.__dto__()
        )._asdict()

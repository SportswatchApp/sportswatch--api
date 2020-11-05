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

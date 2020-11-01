from django.db import models


class Club(models.Model):
    name = models.CharField(
        max_length=120,
        verbose_name='Navn'
    )
    created_date = models.DateTimeField(auto_now_add=True)

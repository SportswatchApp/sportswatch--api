from django.db import models


class Trainee(models.Model):
    member = models.ForeignKey(
        to='app.Member',
        on_delete=models.CASCADE,
        verbose_name='Medlem'
    )

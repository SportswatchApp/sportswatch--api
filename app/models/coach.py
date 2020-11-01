from django.db import models


class Coach(models.Model):
    member = models.ForeignKey(
        to='app.Member',
        on_delete=models.CASCADE,
        verbose_name='Medlem'
    )

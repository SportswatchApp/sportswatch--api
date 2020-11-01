from django.db import models


class Time(models.Model):
    trainee = models.ForeignKey(
        to='app.Trainee',
        on_delete=models.CASCADE,
        verbose_name='Trainee'
    )
    category = models.ForeignKey(
        to='app.Category',
        on_delete=models.PROTECT,
        verbose_name='Kategori'
    )
    time = models.IntegerField(
        verbose_name='Tid sekunder 1/100'
    )
    created_date = models.DateTimeField(auto_now_add=True)

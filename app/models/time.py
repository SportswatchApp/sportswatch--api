from collections import namedtuple

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
    reported_by = models.ForeignKey(
        to='app.User',
        on_delete=models.SET_NULL,
        null=True,
        default=None
    )
    created_date = models.DateTimeField(auto_now_add=True)

    DTO = namedtuple('DTO', 'id trainee category time reported_by created_date')

    def __dto__(self):
        return Time.DTO(
            id=self.id,
            trainee={'id': self.trainee.id},
            category={'id': self.category.id, 'name': self.category.name},
            time=self.time,
            reported_by={'id': self.reported_by.id},
            created_date=self.created_date.__str__()
        )._asdict()

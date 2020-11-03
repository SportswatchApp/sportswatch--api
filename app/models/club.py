from collections import namedtuple

from django.db import models


class Club(models.Model):
    name = models.CharField(
        max_length=120,
        verbose_name='Navn'
    )
    region = models.CharField(max_length=45)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=35)
    country = models.CharField(max_length=35)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('name', 'region', 'zip_code', 'country',)

    DTO = namedtuple('DTO', 'id name region zip_code city country created_date members')

    def has_active_member(self, user):
        return self.member_set.filter(user=user, active=True).exists()

    def has_member(self, user):
        return self.member_set.filter(user=user).exists()

    def __dto__(self):
        return Club.DTO(
            id=self.id,
            name=self.name,
            region=self.region,
            city=self.city,
            zip_code=self.zip_code,
            country=self.country,
            created_date=self.created_date,
            members={'link': '/api/v1/club/' + str(self.id) + '/members/'}
        )._asdict()

from collections import namedtuple

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

    DTO = namedtuple('DTO', 'id email first_name last_name date_joined')

    def __dto__(self):
        return User.DTO(
            id=self.id,
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
            date_joined=self.date_joined
        )._asdict()

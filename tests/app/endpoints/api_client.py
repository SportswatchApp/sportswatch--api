from rest_framework import test
from rest_framework.authtoken.models import Token

from app.models import User


class ApiClient(test.APIClient):

    def __init__(self, enforce_csrf_checks=False, **defaults):
        super().__init__(enforce_csrf_checks, **defaults)
        user = User.objects.create(
            username='A7V1C1mtl1ej7tUDGqY2',
            password='A7V1C1mtl1ej7tUDGqY2'
        )
        token = Token.objects.create(user=user)
        self.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

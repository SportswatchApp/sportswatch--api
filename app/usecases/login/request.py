from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from app.usecases import request


class Request(request.Request):

    required = ('email', 'password',)

    def validate(self):
        self.valid_email(self.body['email'])

    def valid_email(self, email):
        try:
            validate_email(email)
        except ValidationError:
            self.errors.append({
                'status': 400,
                'da': 'Indtast venligst en gyldig email',
                'en': 'Email address is not valid'
            })

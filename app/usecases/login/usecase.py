from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class Login:

    @staticmethod
    def login(request, listener):
        if not request.is_valid:
            listener.handle_invalid_request(request)
            return

        fields = request.body
        email = fields['email']
        password = fields['password']

        user = authenticate(username=email, password=password)
        if user is None:
            listener.handle_invalid_credentials()
        else:
            token, created = Token.objects.get_or_create(user=user)
            listener.handle_success({
                "token": token.key,
                "created": token.created
            })

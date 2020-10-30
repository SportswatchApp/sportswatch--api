from django.db import IntegrityError

from app.models import User


class Create:

    @staticmethod
    def create(request, listener):
        if not request.is_valid:
            listener.handle_invalid_request(request)
            return

        fields = request.body
        first_name = fields['first_name']
        last_name = fields['last_name']
        email = fields['email']
        password = fields['password']

        if User.objects.filter(username=email).exists():
            listener.handle_unique_username()
            return

        try:
            user = User.objects.create_user(
                username=email,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password,
                is_staff=False,
                is_superuser=False
            )
        except IntegrityError as e:
            listener.handle_database_error(str(e))
            return

        listener.handle_success(user.__dto__())

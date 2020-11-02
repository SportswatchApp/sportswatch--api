from rest_framework.authtoken.models import Token


class Logout:

    @staticmethod
    def logout(user, listener):
        if user.is_anonymous:
            listener.handle_anonymous_user()
            return

        Token.objects.filter(user=user.id).delete()
        listener.handle_success({'detail': 'User logged out'})

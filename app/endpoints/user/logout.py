from app.endpoints._mixins.auth import AuthMixin
from app.endpoints.response import Response
from app.usecases import logout


class LogoutEndpoint(AuthMixin):

    def post(self, request):
        user = request.user
        listener = logout.Listener()
        logout.Logout.logout(user, listener)
        return Response(
            request=request,
            listener=listener
        )

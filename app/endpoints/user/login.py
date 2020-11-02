from app.endpoints._mixins.public import PublicMixin
from app.endpoints.response import Response
from app.usecases import login


class LoginEndpoint(PublicMixin):

    request_obj = login.Request

    def post(self, request):
        _request = login.Request().from_django(request)
        listener = login.Listener()
        login.Login.login(_request, listener)
        return Response(
            request=request,
            listener=listener
        )

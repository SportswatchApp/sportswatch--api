from app.endpoints._mixins.auth import AuthMixin
from app.endpoints.response import Response
from app.usecases import create_time


class CreateTimeEndpoint(AuthMixin):

    def post(self, request):
        _request = create_time.Request().from_django(request)
        listener = create_time.Listener()
        create_time.Create.create(_request, listener)
        return Response(
            listener=listener,
            request=request
        )

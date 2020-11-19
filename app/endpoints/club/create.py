from app.endpoints._mixins.auth import AuthMixin
from app.endpoints.response import Response
from app.models import Club
from app.usecases import create_club


class CreateClubEndpoint(AuthMixin):

    def post(self, request):
        _request = create_club.Request().from_django(request)
        listener = create_club.Listener()
        create_club.Create.create(_request, listener)
        return Response(
            request=request,
            listener=listener
        )

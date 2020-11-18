from app.endpoints._mixins.auth import AuthMixin
from app.endpoints.response import Response
from app.usecases import list_clubs


class ListClubsEndpoints(AuthMixin):

    def get(self, request):
        listener = list_clubs.Listener()
        list_clubs.List.list(listener)
        return Response(
            request,
            listener
        )

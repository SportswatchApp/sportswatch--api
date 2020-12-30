from app.endpoints._mixins.auth import AuthMixin
from app.endpoints.response import Response
from app.usecases import list_times


class ListTraineeTimesEndpoint(AuthMixin):

    def get(self, request, trainee_id):
        _request = list_times.Request().from_django(request, extras={'trainee_id': trainee_id})
        listener = list_times.Listener()
        list_times.List.list(_request, listener)
        return Response(
            request=request,
            listener=listener
        )

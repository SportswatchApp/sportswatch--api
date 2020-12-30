from app.endpoints._mixins.auth import AuthMixin
from app.endpoints.response import Response
from app.usecases import get_times


class GetTraineeTimesEndpoint(AuthMixin):

    def get(self, request, trainee_id):
        _request = get_times.Request().from_django(request, extras={'trainee_id': trainee_id})
        listener = get_times.Listener()
        get_times.Get.get(_request, listener)
        return Response(
            request=request,
            listener=listener
        )

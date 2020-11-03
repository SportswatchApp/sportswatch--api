from app.endpoints._mixins.auth import AuthMixin
from app.endpoints.response import Response
from app.usecases import list_trainees


class ListTraineesEndpoint(AuthMixin):

    def get(self, request):
        _request = list_trainees.Request().from_django(request, extras={
            'order_by': request.GET.get('order_by', ''),
            'q': request.GET.get('q', '')
        })
        listener = list_trainees.Listener()
        list_trainees.List.list(_request, listener)
        return Response(
            request=request,
            listener=listener
        )

from app.endpoints._mixins.auth import AuthMixin
from app.endpoints.response import Response
from app.usecases import get_user


class GetUserEndpoint(AuthMixin):

    def get(self, request):
        listener = get_user.Listener()
        get_user.Get.get(request.user, listener)
        return Response(
            request=request,
            listener=listener
        )

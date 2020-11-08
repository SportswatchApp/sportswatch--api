from app.endpoints._mixins.public import PublicMixin
from app.endpoints.response import Response
from app.models import User
from app.usecases import create_user, get_user


class UsersEndpoint(PublicMixin):

    model = User
    request_obj = create_user.Request

    def post(self, request):
        _request = create_user.Request().from_django(request)
        listener = create_user.Listener()
        create_user.Create.create(_request, listener)
        return Response(
            request=request,
            listener=listener
        )

    def get(self, request):
        listener = get_user.Listener()
        get_user.Get.get(request.user, listener)
        return Response(
            request=request,
            listener=listener
        )

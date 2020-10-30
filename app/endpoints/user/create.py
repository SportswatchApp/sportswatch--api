from app.endpoints._mixins.public import PublicMixin
from app.endpoints.response import Response
from app.models import User
from app.usecases import create_user


class CreateUserEndpoint(PublicMixin):

    def post(self, request):
        _request = create_user.Request().from_django(request)
        listener = create_user.Listener()
        create_user.Create.create(_request, listener)
        return Response(
            request=request,
            listener=listener
        )

    def get_model(self):
        return User

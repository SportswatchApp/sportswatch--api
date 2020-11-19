from app.endpoints._mixins.auth import AuthMixin
from app.endpoints.response import Response
from app.usecases import create_category


class CreateCategoryEndPoint(AuthMixin):

    def post(self, request):
        _request = create_category.Request().from_django(request)
        listener = create_category.Listener()
        create_category.Create.create(_request, listener)
        return Response(
            request,
            listener
        )

from app.endpoints._mixins.auth import AuthMixin
from app.endpoints.response import Response
from app.usecases import list_categories


class ListCategoriesEndpoint(AuthMixin):

    def get(self, request, trainee_id):
        listener = list_categories.Listener()
        list_categories.List.list(listener, request, trainee_id)
        return Response(
            request,
            listener
        )

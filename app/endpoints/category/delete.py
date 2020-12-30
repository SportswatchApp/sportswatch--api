from app.endpoints._mixins.auth import AuthMixin
from app.endpoints.response import Response
from app.usecases import delete_category


class DeleteCategory(AuthMixin):
    def delete(self, request, category_id):
        _request = delete_category.Request.from_django(request)
        listener = delete_category.Listener()
        delete_category.delete()
        return Response(
            request=request,
            listener=listener
        )

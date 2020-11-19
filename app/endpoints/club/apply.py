from app.endpoints._mixins.auth import AuthMixin
from app.endpoints.response import Response
from app.usecases import apply_membership


class ApplyMembershipView(AuthMixin):

    def post(self, request, club_id):
        _request = apply_membership.Request().from_django(request, extras={'club_id': club_id})
        listener = apply_membership.Listener()
        apply_membership.Apply.apply(_request, listener)
        return Response(
            request,
            listener
        )

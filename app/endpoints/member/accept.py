from app.endpoints._mixins.auth import AuthMixin
from app.endpoints.response import Response
from app.usecases import accept_membership


class AcceptMembershipEndpoint(AuthMixin):

    def put(self, request, member_id):
        _request = accept_membership.Request().from_django(request, extras={
            'member_id': member_id
        })
        listener = accept_membership.Listener()
        accept_membership.Accept.accept(_request, listener)
        return Response(
            request=request,
            listener=listener
        )

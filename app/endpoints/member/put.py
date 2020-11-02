from app.endpoints._mixins.auth import AuthMixin
from app.endpoints.response import Response
from app.models import Member
from app.usecases import put_member


class PutMemberEndpoint(AuthMixin):

    model = Member
    request_obj = put_member.Request

    def put(self, request, club_id, user_id):
        _request = put_member.Request().from_django(request)
        listener = put_member.Listener()
        put_member.Put.put(club_id, user_id, _request, listener)
        return Response(
            request=request,
            listener=listener
        )

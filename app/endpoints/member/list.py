from app.endpoints._mixins.auth import AuthMixin
from app.endpoints.response import Response
from app.models import Member
from app.usecases import get_members


class ListMembersEndpoint(AuthMixin):

    model = Member

    def get(self, request, club_id):
        listener = get_members.Listener()
        get_members.Get.get(club_id, request.user, listener)
        return Response(
            request=request,
            listener=listener
        )

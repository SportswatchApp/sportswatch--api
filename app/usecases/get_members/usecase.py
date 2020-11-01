from app.models import Club, Member


class Get:

    @staticmethod
    def get(club_id, user, listener):
        try:
            club = Club.objects.get(pk=club_id)
        except Club.DoesNotExist:
            listener.handle_not_found()
            return

        if not club.has_member(user):
            listener.handle_forbidden()
            return

        members = club.member_set.filter(active=True)
        listener.handle_success(Member.__dtolist__(members))

from app.models import Club, Member, Admin


class Create:

    @staticmethod
    def create(request, listener):
        if not request.is_valid:
            listener.handle_invalid_request(request)
            return

        fields = request.body
        name = fields['name']
        user = request.user

        club = Club.objects.create(name=name)
        member = Member.objects.create(
            club=club,
            user=user,
            active=True,
            invited_by=None
        )
        Admin.objects.create(
            member=member
        )
        listener.handle_success(club.__dto__())

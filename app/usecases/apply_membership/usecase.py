from django.db import IntegrityError

from app.models import Member, Club, Trainee


class Apply:

    @staticmethod
    def apply(request, listener):
        fields = request.body
        club_id = fields['club_id']
        user = request.user

        try:
            club = Club.objects.get(pk=club_id)
        except Club.DoesNotExist:
            listener.handle_not_found()
            return

        if user.is_member_of(club):
            listener.handle_already_applied()
            return

        try:
            member = Member.objects.create(
                active=False,
                marked_spam=False,
                club=club,
                invited_by=user,
                user=user
            )
            Trainee.objects.create(
                member_id=member.id
            )
            listener.handle_success(member.__dto__())
        except IntegrityError as e:
            listener.handle_database_error(e)

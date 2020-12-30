from django.db import IntegrityError
from app.models import Category, Club


class Create:

    @staticmethod
    def create(request, listener):
        if not request.is_valid:
            listener.handle_invalid_request(request)
            return

        fields = request.body
        name = fields['name']
        club_id = fields['club_id']

        try:
            club = Club.objects.get(pk=club_id)
        except Club.DoesNotExist:
            listener.handle_club_not_found()
            return

        if not request.user.admin_of(club):
            listener.handle_user_must_be_admin_of_club()
            return

        if Category.objects.filter(name=name, club_id=club_id).exists():
            listener.handle_already_exist()
            return

        try:
            category = Category.objects.create(
                name=name,
                club_id=club_id
            )
        except IntegrityError as e:
            listener.handle_database_error(str(e))
            return

        listener.handle_success(category.__dto__())

        



from app.models import Category, Trainee


class List:

    @staticmethod
    def list(listener, request, trainee_id):
        try:
            trainee = Trainee.objects.get(id=trainee_id)
        except Trainee.DoesNotExist:
            listener.handle_not_found()
            return

        if not request.user.can_register_for(trainee):
            return

        club = trainee.member.club
        categories = Category.objects.filter(club_id=club.id)

        if len(categories) == 0:
            listener.handle_no_categories()
            return

        listener.handle_success(Category.__dtolist__(categories=categories))

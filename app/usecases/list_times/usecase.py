from app.models import Trainee, Time


class List:

    @staticmethod
    def list(request, listener):
        fields = request.body
        user = request.user
        trainee_id = fields['trainee_id']

        try:
            trainee = Trainee.objects.get(pk=trainee_id)
        except Trainee.DoesNotExist:
            listener.handle_not_found()
            return

        trainee_club = trainee.member.club
        if trainee.member.user.pk == user.pk \
                or user.coach_of(trainee_club) \
                or user.admin_of(trainee_club) \
                or user.is_trusted_by(trainee):
            listener.handle_success(Time.__dtolist__(trainee.time_set.all()))
        else:
            listener.handle_forbidden()

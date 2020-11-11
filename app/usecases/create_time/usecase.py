from django.db import IntegrityError

from app.models import Time, Trainee, Category


class Create:

    @staticmethod
    def create(request, listener):
        if not request.is_valid:
            listener.handle_invalid_request(request)
            return

        fields = request.body
        time = fields['time']
        trainee_id = fields['trainee_id']
        category_id = fields['category_id']
        reported_by = request.user

        try:
            trainee = Trainee.objects.get(pk=trainee_id)
        except Trainee.DoesNotExist:
            listener.handle_trainee_not_found()
            return

        if not reported_by.can_register_for(trainee):
            listener.handle_forbidden()
            return

        if not Category.objects.filter(club=trainee.member.club, pk=category_id).exists():
            listener.handle_illegal_category()
            return

        try:
            time = Time.objects.create(
                time=time,
                trainee_id=trainee_id,
                category_id=category_id,
                reported_by=reported_by
            )
            listener.handle_success(time.__dto__())
        except IntegrityError as e:
            _str = str(e)
            print(_str)

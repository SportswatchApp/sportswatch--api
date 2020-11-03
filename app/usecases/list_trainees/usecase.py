from django.db.models import Q, Sum, Case, When, IntegerField
from django.db.models.functions import Concat

from app.models import Trainee


class List:

    @staticmethod
    def list(request, listener):
        if not request.is_valid:
            listener.handle_invalid_request(request)
            return

        fields = request.body
        order_by = fields['order_by']
        keyword = List._filter(fields['q'])
        user = request.user

        search = (Q(fullname__icontains=keyword) |
                  Q(member__user__username__icontains=keyword) |
                  (Q(member__user_id=keyword) if List._represents_int(keyword) else Q())) if keyword != '' else Q()

        sum_registrations = Sum(
            Case(When(time__reported_by=user, then=1)), output_field=IntegerField()
        )

        trainees = Trainee.objects.annotate(
            fullname=Concat('member__user__first_name', 'member__user__last_name'),
            num_registrations=sum_registrations
        ).filter(
            (Q(member__club__in=user.clubs()) | Q(member__club__trusted_users=user)) & search
        )

        if order_by == 'frequently':
            trainees.order_by('-num_registrations').distinct()
        else:
            trainees.distinct()

        listener.handle_success(Trainee.__dtolist__(trainees))

    @staticmethod
    def _represents_int(val):
        try:
            int(val)
            return True
        except ValueError:
            return False

    @staticmethod
    def _filter(_str):
        if len(_str) > 1:
            return _str.replace(' ', '')[:45]
        else:
            return ''

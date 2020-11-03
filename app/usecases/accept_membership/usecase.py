from app.models import Member


class Accept:

    @staticmethod
    def accept(request, listener):
        if not request.is_valid:
            listener.handle_invalid_request(request)
            return

        fields = request.body
        member_id = fields['member_id']
        user = request.user

        try:
            member = Member.objects.get(pk=member_id)
            if not member.user == user:
                listener.handle_forbidden()
                return
            member.active = True
            member.save()
            listener.handle_success({'detail': 'Membership accepted'})
        except Member.DoesNotExist:
            listener.handle_member_not_found()

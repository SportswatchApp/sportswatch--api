from app.models import Club, User, Member


class Put:

    @staticmethod
    def put(club_id, user_id, request, listener):
        if not request.is_valid:
            listener.handle_invalid_request(request)
            return

        try:
            club = Club.objects.get(pk=club_id)
        except Club.DoesNotExist:
            listener.handle_club_not_found()
            return

        try:
            user_to_put = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            listener.handle_user_not_found()
            return

        fields = request.body
        roles = fields['roles']
        user = request.user
        is_admin = user.admin_of(club)
        is_coach = user.coach_of(club)

        if not is_admin and not is_coach:
            listener.handle_forbidden()
            return

        for role in roles:
            if role not in Member.ROLES:
                listener.handle_illegal_role(role)
                return

        if (is_coach and not is_admin) and 'admin' in roles:
            listener.handle_forbidden_coach_action()
            return
        else:
            member, created = Member.objects.get_or_create(
                user_id=user_to_put.id,
                club_id=club_id,
                defaults={
                    'invited_by': user,
                    'club': club
                }
            )
            if 'admin' in roles:
                member.set_admin(True)
            elif not created:
                member.set_admin(False)
            else:
                pass

            if 'coach' in roles:
                member.set_coach(True)
            elif not created:
                member.set_coach(False)
            else:
                pass

            if 'trainee' in roles:
                member.set_trainee(True)
            elif not created:
                member.set_trainee(False)
            else:
                pass

            listener.handle_success((created, member.__dto__()))

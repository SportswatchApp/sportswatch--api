from django.db import IntegrityError

from app.models import Club, Member, Admin


class Create:

    @staticmethod
    def create(request, listener):
        if not request.is_valid:
            listener.handle_invalid_request(request)
            return

        fields = request.body
        name = fields['name']
        city = fields['city']
        zip_code = fields['zip_code']
        country = fields['country']
        region = fields['region']
        user = request.user
        try:
            club = Club.objects.create(
                name=name,
                city=city,
                zip_code=zip_code,
                country=country,
                region=region
            )
        except IntegrityError as e:
            _str = str(e)
            if 'constraint failed' in _str:
                listener.handle_already_exist()
            else:
                listener.handle_database_error()
            return

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

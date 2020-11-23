from django.db import IntegrityError
from app.models import Category


class Create:

    @staticmethod
    def create(request, listener):
        if not request.is_valid:
            listener.handle_invalid_request(request)
            return

        fields = request.body
        name = fields['name']

        try:
            category = Category.objects.create(
                name=name
            )
        except IntegrityError as e:
            _str = str(e)
            if 'constraint failed' in _str:
                listener.handle_already_exist()
            else:
                listener.handle_database_error()
            return

        



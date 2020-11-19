from app.models import Club


class List:

    @staticmethod
    def list(listener):
        listener.handle_success(Club.__dtolist__(Club.objects.all()))

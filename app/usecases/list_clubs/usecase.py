from app.models import Club


class List:

    @staticmethod
    def list(listener):
        listener.handle_success([c.__dto__() for c in Club.objects.all()])

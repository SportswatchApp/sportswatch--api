from app.models import Category, Trainee


class List:

    @staticmethod
    def list(listener, request, trainee_id):

        trainee = Trainee.objects.get(trainee_id)

        listener.handle_success(Category.__dtolist__(Category.objects.all()))

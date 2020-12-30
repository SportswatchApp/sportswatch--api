from app.usecases import request


class Request(request.Request):

    required = ('trainee_id',)

    def validate(self):
        pass

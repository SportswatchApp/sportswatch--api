from app.usecases import request


class Request(request.Request):

    parameters = {}

    def validate(self):
        pass

from app.usecases import request


class Request(request.Request):
    required = ()
    optional = ()

    def validate(self):
        pass

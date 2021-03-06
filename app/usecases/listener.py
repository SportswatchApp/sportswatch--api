class Listener:
    response = tuple()

    def handle_invalid_request(self, request):
        self.response = request.get_error()

    def handle_database_error(self, exception):
        self.response = (500, 'Internal server error')

    def get_response(self):
        return self.response

    def detail_maker(self, msg: str, status: int):
        return {
            'status': status,
            'detail': msg
        }


class ForbiddenListener:
    def handle_forbidden(self, data=None):
        raise NotImplementedError()


class SuccessListener:
    def handle_success(self, data=None):
        raise NotImplementedError()


class NotFoundListener:
    def handle_not_found(self):
        raise NotImplementedError()


class DatabaseListener:
    def handle_database_error(self, msg=None):
        raise NotImplementedError()

import json


class Request:

    required = tuple()
    optional = tuple()

    def __init__(self) -> None:
        self.body = {}
        self.is_valid = True
        self.errors = []
        self.user = None

    def from_dict(self, _dict):
        self.body = _dict
        self._validate_required()
        if not self.errors:
            self.validate()

        if not self.errors:
            self.is_valid = True
        else:
            self.is_valid = False

        return self

    def from_django(self, request, extras=None):
        decoded = request.body.decode('utf-8')
        self.user = request.user
        try:
            if decoded:
                _dict = json.loads(decoded)
            else:
                _dict = {}
            if extras:
                _dict = {**_dict, **extras}
            return self.from_dict(_dict)
        except json.decoder.JSONDecodeError:
            self.is_valid = False
            self.errors.append((
                400, 'Provide a valid body in content_type: application/json'
            ))
            return self

    def get_error(self):
        return self.errors.pop()

    def validate(self):
        raise NotImplementedError()

    def _validate_required(self):
        for r in self.required:
            try:
                self.body[r]
            except KeyError:
                self.errors.append((
                    400, 'Missing required field: ' + r
                ))

    def is_integer(self, val):
        try:
            int(val)
            return True
        except TypeError:
            return False

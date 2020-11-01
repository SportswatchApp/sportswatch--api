import json


class Request:

    required = tuple()
    optional = tuple()

    def __init__(self) -> None:
        self.body = {}
        self.is_valid = True
        self.errors = []

    def from_body(self, body):
        try:
            self.body = json.loads(body.decode('utf-8'))
            self._validate_required()
            if not self.errors:
                self.validate()

            if not self.errors:
                self.is_valid = True
            else:
                self.is_valid = False
        except json.decoder.JSONDecodeError:
            self.is_valid = False
            self.errors.append((
                400, 'Provide a valid body in content_type: application/json'
            ))
        return self

    def from_django(self, request):
        return self.from_body(request.body)

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

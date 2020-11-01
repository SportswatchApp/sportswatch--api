from app.usecases import request


class Request(request.Request):

    required = ('roles',)

    def validate(self):
        if not self.body['roles']:
            self.errors.append({
                'status': 400,
                'da': 'Mindst én rolle skal vælges',
                'en': 'At least one role should be provided'
            })

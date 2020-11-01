from app.usecases import request


class Request(request.Request):

    required = ('name',)

    def validate(self):
        if not self.body['name']:
            self.errors.append({
                'status': 400,
                'da': 'Klubnavn må ikke være tomt',
                'en': 'Club name can not be empty'
            })

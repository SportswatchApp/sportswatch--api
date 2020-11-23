from app.usecases import request


class Request(request.Request):
    required = ('name',)

    def validate(self):
        category_name = self.body['name']
        if not category_name :
            self.errors.append({
             'status': 400,
             'da': '',
             'en': ''
            })

from app.usecases import request


class Request(request.Request):

    required = 'trainee_id'

    def validate(self):
        trainee_id = self.body['trainee_id']
        if not trainee_id:
            self.errors.append({
                'status': 400,
                'da': 'Der skal medsendes en trainee',
                'en': 'There must be a trainee'
            })

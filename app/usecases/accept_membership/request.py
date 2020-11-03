from app.usecases import request


class Request(request.Request):

    def validate(self):
        member_id = self.body['member_id']
        if not self.is_integer(member_id):
            self.errors.append({
                'status': 400,
                'da': 'Medlems ID skal være et heltal',
                'en': 'Memeber id must be of type integer'
            })

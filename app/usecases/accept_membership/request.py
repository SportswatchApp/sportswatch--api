from app.usecases import request


class Request(request.Request):

    def validate(self):
        member_id = self.body['member_id']
        try:
            int(member_id)
        except TypeError:
            self.errors.append({
                'status': 400,
                'da': 'Medlems ID skal være et heltal',
                'en': 'Memeber id must be of type integer'
            })

from app.usecases import request


class Request(request.Request):

    def validate(self):
        time = self.body['time']
        try:
            _t = int(time)
            if _t <= 0:
                self.errors.append({
                    'status': 400,
                    'da': 'Tiden skal angives i 100-dele større end 0',
                    'en': 'Time must be provided as a positive integer in 1/100'
                })
        except (TypeError, ValueError):
            self.errors.append((
                400, 'Time must be provided as an integer'
            ))

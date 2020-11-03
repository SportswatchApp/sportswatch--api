from app.usecases import request


class Request(request.Request):

    required = ('name', 'city', 'country', 'zip_code', 'region')

    def validate(self):
        if not self.body['name']:
            self.errors.append({
                'status': 400,
                'da': 'Klubnavn må ikke være tomt',
                'en': 'Club name can not be empty'
            })

        if not self.body['city']:
            self.errors.append({
                'status': 400,
                'da': 'By skal udfyldes',
                'en': 'City can not be empty'
            })

        if not self.body['zip_code']:
            self.errors.append({
                'status': 400,
                'da': 'Post nr. skal udfyldes',
                'en': 'Zip code can not be empty'
            })

        if not self.body['region']:
            self.errors.append({
                'status': 400,
                'da': 'Region skal udfyldes',
                'en': 'Region can not be empty'
            })

        if not self.body['country']:
            self.errors.append({
                'da': 'Land skal udfyldes',
                'en': 'Coyntry can not be empty'
            })

from app.usecases import request


class Request(request.Request):

    required = (
        'first_name',
        'last_name',
        'email',
        'password',
        'conf_password'
    )

    def validate(self):
        fields = self.body
        password = fields['password']
        conf_password = fields['conf_password']
        if password != conf_password:
            self.errors.append({
                'status': 400,
                'da': 'Adgangskoderne matcher ikke hinanden',
                'en': 'Passwords are not identical'
            })

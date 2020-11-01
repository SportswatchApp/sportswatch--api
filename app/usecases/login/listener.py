from app.usecases import listener


class Listener(listener.Listener, listener.SuccessListener):

    def handle_success(self, key):
        self.response = (202, key)

    def handle_invalid_credentials(self):
        self.response = {
            'status': 401,
            'en': 'Invalid credentials',
            'da': 'E-mail eller adgangskode er forkert'
        }

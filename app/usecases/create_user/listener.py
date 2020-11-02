from app.usecases import listener


class Listener(listener.Listener, listener.SuccessListener):

    def handle_success(self, data=None):
        self.response = (
            201, data
        )

    def handle_unique_username(self):
        self.response = {
            'status': 409,
            'da': 'E-mailen er allerede i brug',
            'en': 'E-mail already in use'
        }

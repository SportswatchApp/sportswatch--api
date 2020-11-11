from app.usecases import listener


class Listener(listener.Listener, listener.SuccessListener, listener.NotFoundListener):

    def handle_success(self, data=None):
        self.response = (200, data)

    def handle_not_found(self):
        self.response = {
            'status': 400,
            'en': 'User not found',
            'da': 'Brugeren blev ikke fundet'
        }

from app.usecases import listener


class Listener(listener.Listener, listener.SuccessListener, listener.NotFoundListener):

    def handle_success(self, data=None):
        self.response = (200, data)

    def handle_not_found(self):
        self.response = {
            'status': 404,
            'en': 'Club not found',
            'da': 'Klubben findes ikke'
        }

    def handle_forbidden(self):
        self.response = {
            'status': 403,
            'en': 'You do not have permission to see these members',
            'da': 'Du har ikke adgang til disse medlemmer'
        }

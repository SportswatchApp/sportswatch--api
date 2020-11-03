from app.usecases import listener


class Listener(listener.Listener, listener.SuccessListener, listener.ForbiddenListener):

    def handle_success(self, data=None):
        self.response = (202, data)

    def handle_forbidden(self, data=None):
        self.response = {
            'status': 403,
            'en': 'You do not have permission to do this',
            'da': 'Du har ikke adgang til at acceptere dette medlemsskab'
        }

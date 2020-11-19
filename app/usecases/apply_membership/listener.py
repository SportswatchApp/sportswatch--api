from app.usecases import listener


class Listener(listener.Listener, listener.SuccessListener, listener.NotFoundListener):

    def handle_success(self, data=None):
        self.response = (200, data)

    def handle_already_applied(self):
        self.response = {
            'status': 208,
            'da': self.detail_maker('Du kan kun ansøge én gang', 208),
            'en': self.detail_maker('Application already reported', 208)
        }

    def handle_not_found(self):
        self.response = {
            'status': 404,
            'da': 'Klub blev ikke fundet',
            'en': 'Club not found'
        }

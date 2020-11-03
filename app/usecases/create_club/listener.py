from app.usecases import listener


class Listener(listener.Listener, listener.SuccessListener):

    def handle_success(self, data=None):
        self.response = (201, data)

    def handle_already_exist(self):
        self.response = {
            'status': 409,
            'da': 'Klubben findes allerede',
            'en': 'The club already exist'
        }

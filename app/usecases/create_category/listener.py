from app.usecases import listener


class Listener(listener.Listener, listener.SuccessListener):

    def handle_success(self, data=None):
        self.response = (201, data)

    def handle_already_exist(self):
        self.response = {
            'status': 409,
            'da': 'Kategorien eksistere allerede',
            'en': 'The category already exsists'
        }

    def handle_club_does_not_exist(self):
        self.response = {
            'status': 409,
            'da': 'Klubben eksistere ikke',
            'en': 'The club does not exists'
        }
from app.usecases import listener


class Listener(listener.Listener, listener.SuccessListener):

    def handle_success(self, data=None):
        self.response = (200, data)

    def handle_not_found(self):
        self.response = {
            'status': 404,
            'en': 'Trainee not found',
            'da': 'Traniee findes ikke'
        }
    def handle_no_categories(self):
        self.response = {
            'status': 404,
            'en': 'No categories found',
            'da': 'Der kunne ikke findes nogle kategorier'
        }
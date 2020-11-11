from app.usecases import listener


class Listener(listener.Listener, listener.SuccessListener, listener.ForbiddenListener):

    def handle_success(self, data=None):
        self.response = (201, data)

    def handle_forbidden(self, data=None):
        self.response = {
            'status': 403,
            'da': 'Du har ikke adgang til at registere tider for denne udøver',
            'en': 'You do not have permission to register times for this trainee'
        }

    def handle_illegal_category(self):
        self.response = {
            'status': 404,
            'da': 'Kategorien blev ikke fundet',
            'en': 'Category not found'
        }

    def handle_trainee_not_found(self):
        self.response = {
            'status': 404,
            'da': 'Udøveren blev ikke fundet',
            'en': 'Trainee not found'
        }

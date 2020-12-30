from app.usecases import listener


class Listener(
    listener.Listener,
    listener.SuccessListener,
    listener.NotFoundListener,
    listener.ForbiddenListener
):

    def handle_success(self, data=None):
        self.response = (200, data)

    def handle_not_found(self):
        self.response = {
            'status': 404,
            'da': 'Udøveren findes ikke',
            'en': 'Trainee not found'
        }

    def handle_forbidden(self, data=None):
        self.response = {
            'status': 403,
            'da': 'Du har ikke adgang til at se tider for denne udøver',
            'en': 'You do not have access to list times for this trainee'
        }

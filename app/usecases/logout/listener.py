from app.usecases import listener


class Listener(listener.Listener, listener.SuccessListener):

    def handle_success(self, data=None):
        self.response = (205, data)

    def handle_anonymous_user(self):
        self.response = (401, 'Not authorized')

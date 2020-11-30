from app.usecases import listener


class Listener(listener.Listener, listener.SuccessListener):
    def handle_success(self, data=None):
        self.response = (201, data)

from app.usecases import listener


class Listener(listener.Listener, listener.SuccessListener, listener.NotFoundListener):
    pass

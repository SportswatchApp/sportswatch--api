class Get:

    @staticmethod
    def get(user, listener):
        if user.is_anonymous:
            listener.handle_not_found()
        else:
            listener.handle_success(user.__dto__())

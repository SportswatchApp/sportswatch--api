from app.usecases import listener


class Listener(listener.Listener, listener.SuccessListener):

    def handle_success(self, data=None):
        self.response = (201, data)

    def handle_already_exist(self):
        self.response = {
            'status': 409,
            'da': 'Kategorien eksistere allerede',
            'en': 'The category already exists'
        }

    def handle_club_not_found(self):
        self.response = {
            'status': 404,
            'da': 'Klubben eksistere ikke',
            'en': 'The club does not exists'
        }

    def handle_user_must_be_admin_of_club(self):
        self.response = {
            'status': 403,
            'da': 'Du skal være admin af den klub du vil oprette en kategori for',
            'en': 'You must be a admin of the club you are trying to create a category for'
        }

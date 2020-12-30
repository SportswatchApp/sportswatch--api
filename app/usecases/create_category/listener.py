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

    def handle_user_must_be_member_of_club(self):
        self.response = {
            'status': 403,
            'da': 'Du skal være medlem af den klub du vil oprette en kategori for',
            'en': 'You must be a member of the club you are trying to create a category for'
        }

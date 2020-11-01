from app.usecases import listener


class Listener(listener.Listener, listener.SuccessListener):

    def handle_club_not_found(self):
        self.response = {
            'status': 404,
            'da': 'Klubben findes ikke',
            'en': 'Club not found'
        }

    def handle_user_not_found(self):
        self.response = {
            'status': 404,
            'da': 'Brugeren findes ikke',
            'en': 'User not found'
        }

    def handle_forbidden(self):
        self.response = {
            'status': 403,
            'da': 'Kun trænere og administratorer kan tilføje nye medlemmer',
            'en': 'Only coaches and admins are allowed to add new members'
        }

    def handle_illegal_role(self, role):
        self.response = {
            'status': 400,
            'da': 'Ugyldig rolle',
            'en': 'Invalid role'
        }

    def handle_forbidden_coach_action(self):
        self.response = {
            'status': 403,
            'da': 'Trænere kan ikke tilføje administratorer',
            'en': 'Coaches cannot add admins'
        }

    def handle_success(self, data=None):
        created, entity = data
        self.response = (
            201 if created else 200,
            entity
        )

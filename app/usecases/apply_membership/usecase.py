class Apply:

    @staticmethod
    def apply(request, listener):
        fields = request.body
        club_id = fields['club_id']
        user = request.user

        pass

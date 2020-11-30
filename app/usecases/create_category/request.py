from app.usecases import request


class Request(request.Request):
    required = ('name', 'club_id')

    def validate(self):
        category_name = self.body['name']
        if not category_name :
            self.errors.append({
             'status': 400,
             'da': 'Kategori navn må ikke være tomt',
             'en': 'Category name must not be empty'
            })

        if not self.body['club_id']:
            self.errors.append({
                'status' : 400,
                'da': 'En kategori skal tilhøre en klub',
                'en': 'A category must belong to a club'
            })

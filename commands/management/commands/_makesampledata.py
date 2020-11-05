import os

from django.core import serializers

from sportswatch import settings


class MakeSampleData:
    files = [
        'users.json',
        'tokens.json',
        'clubs.json',
        'members.json',
        'coaches.json',
        'trainees.json',
        'admins.json',
        'categories.json'
    ]
    path = 'tests/media/sample_data'

    def make(self, stdout, style):
        if settings.DEBUG is False:
            raise EnvironmentError('Can only provide sample data when settings.DEBUG = True')

        if settings.DATABASES['default']['ENGINE'] != 'django.db.backends.sqlite3':
            raise EnvironmentError(
                'Please use sqlite3 for sample data or make sure this is a test environment. ' +
                'You can remove this check if you are using mysql.'
            )

        for f in self.files:
            with open(os.path.join(self.path, f)) as file:
                data = file.read()

            for obj in serializers.deserialize("json", data):
                obj.save()

            stdout.write(style.SUCCESS('OK') + ' ' + f)

        stdout.write(
            '\nNow you can run ' + style.SQL_FIELD('python manage.py runserver')
        )

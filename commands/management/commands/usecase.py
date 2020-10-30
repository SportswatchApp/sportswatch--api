from django.core.management import BaseCommand

from commands.build_usecase import build_usecase


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('type', nargs=1, type=str)
        parser.add_argument('name', nargs=1, type=str)

        # Named (optional) arguments
        parser.add_argument(
            '--request',
            action='store_true',
        )

    def handle(self, *args, **options):
        _options = {
            'name':  options['name'][0],
            'type': options['type'][0],
            'request': True if options['request'] else False
        }
        try:
            build_usecase(_options)
            self.stdout.write(self.style.SUCCESS('Usecase "' + _options["name"] + '" is created'))
        except FileExistsError:
            self.stdout.write(self.style.ERROR('Usecase with name "' + _options["name"] + '" already exists'))

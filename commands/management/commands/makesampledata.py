from django.core.management import BaseCommand

from commands.management.commands._makesampledata import MakeSampleData


class Command(BaseCommand):

    def handle(self, *args, **options):
        MakeSampleData().make(self.stdout, self.style)

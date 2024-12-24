from django.core.management.base import BaseCommand
from db.models import Master


class Command(BaseCommand):

    def handle(self, *args, **options):
        Master.objects.create(name=options['name'],
                              skills=options['skills'],
                              login=options['login'],
                              password=options['password'])

    def add_arguments(self, parser):
        parser.add_argument("--name", type=str)
        parser.add_argument("--skills", type=str)
        parser.add_argument("--login", type=str)
        parser.add_argument("--password", type=str)

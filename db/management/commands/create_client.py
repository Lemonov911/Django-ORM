from django.core.management.base import BaseCommand
from db.models import Client


class Command(BaseCommand):

    def handle(self, *args, **options):
        Client.objects.create(fullName=options['fullName'][1], phoneNumber=options['phoneNumber'][0])

    def add_arguments(self, parser):
        parser.add_argument("fullName", nargs="+", type=str)
        parser.add_argument("phoneNumber", nargs="+", type=str)

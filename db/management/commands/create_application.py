from django.core.management.base import BaseCommand
from db.models import Application, Car, Client, Master


class Command(BaseCommand):

    def handle(self, *args, **options):
        Application.objects.create(date=options['date'],
                                   description=options['description'],
                                   status=options['status'],
                                   car=Car.objects.get(id=options['idCar']),
                                   client=Client.objects.get(id=options['idClient']),
                                   master=Master.objects.get(id=options['idMaster'])
                                   )

    def add_arguments(self, parser):
        parser.add_argument("--date", type=str)
        parser.add_argument("--description", type=str)
        parser.add_argument("--status", type=str)
        parser.add_argument("--idCar", type=str)
        parser.add_argument("--idClient", type=str)
        parser.add_argument("--idMaster", type=str)

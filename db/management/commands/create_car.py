from django.core.management.base import BaseCommand
from db.models import Car


class Command(BaseCommand):

    def handle(self, *args, **options):
        Car.objects.create(brand=options['brand'][1], model=options['model'][0])

    def add_arguments(self, parser):
        parser.add_argument("brand", nargs="+", type=str)
        parser.add_argument("model", nargs="+", type=str)

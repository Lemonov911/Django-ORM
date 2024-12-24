from django.core.management.base import BaseCommand
from db.models import Car


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for c in Car.objects.all():
            print(f'ID: {c.id} \tbrand: {c.brand} \tModel: {c.model}')

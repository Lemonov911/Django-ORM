from django.core.management.base import BaseCommand
from db.models import Client


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for c in Client.objects.all():
            print(f'ID: {c.id} \tfullName: {c.fullName} \tModel: {c.phoneNumber}')

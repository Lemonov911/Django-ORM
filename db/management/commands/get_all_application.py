from django.core.management.base import BaseCommand
from db.models import Application


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for a in Application.objects.all():
            print(f'ID: {a.id} \tDate: {a.date} \tDescription: {a.description} \tStatus: {a.status}')

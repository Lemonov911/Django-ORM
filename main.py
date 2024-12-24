############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys

sys.dont_write_bytecode = True

# Import settings
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# setup django environment
import django

django.setup()

# Import your models for use in your script
from db.models import *

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """

# Seed a few users in the database
# User.objects.create(name='Dan')
# User.objects.create(name='Robert')


# Client.objects.create(fullName='Игорь', phoneNumber='88005553535')
# Master.objects.create(name='Иван', skills='Рихтовщик', login='Ivan', password='0000')
# Car.objects.create(brand='Toyota', model='Camry 3.5')
# Application.objects.create(date='25.12.2024', description='Помял крыло', status='В работе',
#                            car=(Car.objects.get(brand='Toyota', model='Camry 3.5')),
#                            client=(Client.objects.get(fullName='Игорь')),
#                            master=(Master.objects.get(login='Ivan')))

for a in Application.objects.all():
    print(f'ID: {a.id} \tDate: {a.date} \tDescription: {a.description} \tStatus: {a.status}')

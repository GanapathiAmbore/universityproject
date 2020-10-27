from django.core.management.base import BaseCommand
from university_app.models import University
import random

class Command(BaseCommand):
    def handle(self, *args, **options):
        names=['JNUTH','OU','KU','JNTUA','HCU']
        types=['Central','State']
        for num in range(10):
            university_names=random.choice(names)
            type_choices=random.choice(types)
            data=University.objects.bulk_create([University(name=university_names,type=type_choices)])


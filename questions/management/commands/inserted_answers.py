from django.core.management.base import BaseCommand
from questions.models import Answer
import random

class Command(BaseCommand):
    def handle(self, *args, **options):
        #users=['Ram','Shayam','Somesh']
        answers=['Hyderabad','Islamabad','Delhi']
        for each in range(100):
            answer=random.choice(answers)
            #answerd_user=random.choice(users)
            data=Answer.objects.bulk_create([Answer(answer=answer)])
        print("{} answers inserted Succesfully!".format(each))

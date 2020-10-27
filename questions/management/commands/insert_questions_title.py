from django.core.management.base import BaseCommand
from questions.models import Question
import random

class Command(BaseCommand):
    def handle(self, *args, **options):
        questions=['what is the capital of India','what is the capital of Telangana','what is the capital of Pakisthan']
        for each in range(100):
            title=random.choice(questions)
            data=Question.objects.bulk_create([Question(title=title)])
        print("{} questions inserted Succesfully!".format(each))

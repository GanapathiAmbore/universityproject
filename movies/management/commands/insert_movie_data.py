from django.core.management.base import BaseCommand
from movies.models import Movie
import random

class Command(BaseCommand):
    def handle(self, *args, **options):
        movies=['BB1','BB2','ALVP','SNK']
        director=['SSR','TS','SSR','ARV']
        genere=['action','drama','fiction','thirller']
        for data in range(21):
            movie=random.choice(movies)
            dir=random.choice(director)
            gen=random.choice(genere)
            movies_data=Movie.objects.bulk_create([Movie(name=movie,director=dir,genere=gen)])
        print("records inserted-->",data)


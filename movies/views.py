from django.shortcuts import render

# Create your views here.
from movies.models import Movie
from movies.forms import MovieForm
from django.db.models import Q


def movie(request):
    director_query = request.GET.get('director')
    movie_query = request.GET.get('movie')
    print("director--->", director_query)
    qs = Movie.objects.all()
    director = qs.filter(director__icontains=director_query)
    movie = qs.filter(name__icontains=movie_query)
    context = {
        'movies': director,
        'director': director_query,
        'movie': movie_query
    }
    return render(request, 'movies/home.html', context)

def movie_search(request):
    if request.method=='GET':
        form=MovieForm()
        director=request.GET.get('director',None)
        movie=request.GET.get('movie',None)
        dir_result=Movie.objects.filter(Q(director=director)|Q(name=movie))
        return render(request,'movies/add_movie.html',{'form':form,'results':dir_result})
    else:
        form=MovieForm()
    return render(request,'movies/add_movie.html',{'form':form})

def add_movie(request):
    return render(request,'add')


from django.urls import path
from movies import views
urlpatterns = [
    path('',views.movie,name='home'),
    path('search/',views.movie_search,name='search')
]

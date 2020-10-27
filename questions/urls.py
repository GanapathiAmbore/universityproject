
from django.urls import path
from questions import views
urlpatterns = [
    path('',views.home,name='home'),
    path('questions/',views.questions,name='questions')

]
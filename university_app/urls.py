from django.urls import path
from university_app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('adduniversity/',views.adduniversity,name='adduniversity')
]

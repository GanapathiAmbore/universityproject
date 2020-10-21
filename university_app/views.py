from django.shortcuts import render
from university_app.models import University,College

def home(request):
    universities=University.objects.all()
    return render(request,'home.html',{'universities':universities})


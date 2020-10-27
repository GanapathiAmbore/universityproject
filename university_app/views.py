from django.shortcuts import render
from university_app.models import College
from university_app.forms import UniversityForm

def home(request):
    universities=College.objects.filter(name='mallareddy')
    return render(request,'university/home.html',{'universities':universities})

def adduniversity(request):
    form=UniversityForm()
    return render(request,'university/add_university_form.html',{'form':form})



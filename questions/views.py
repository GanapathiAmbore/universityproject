from django.http import JsonResponse
from django.shortcuts import render
from questions.serializers import QuestionSerializers
from questions.models import Question
from rest_framework.decorators import api_view
from rest_framework.response import Response

def home(request):
    return render(request,'questions/home.html')

@api_view(['GET','POST'])
def questions(request):
    queryset=Question.objects.all()
    serializers=QuestionSerializers(queryset,many=True)
    return JsonResponse(serializers.data,safe=False)



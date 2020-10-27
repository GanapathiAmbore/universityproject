from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    asked_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)


class Answer(models.Model):
    answer = models.CharField(max_length=200, null=True, blank=True)
    answerd_user = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)

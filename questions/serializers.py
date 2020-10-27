from questions.models import Question
from rest_framework import serializers

class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields='__all__'

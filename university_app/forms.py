from django import forms
from university_app.models import College


class UniversityForm(forms.ModelForm):
    class Meta:
        model = College
        fields = '__all__'

from django import forms
from movies.models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].queryset = Movie.objects.all()
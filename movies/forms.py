from django import forms
from movies.models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
        widgets = {
            "genre": forms.Select(attrs={"class": "form-select"})
        }
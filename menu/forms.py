from django.contrib.auth.forms import UserCreationForm
from django import forms
from menu.models import Cook


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Cook
        fields = UserCreationForm.Meta.fields + ("years_of_experience",)


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
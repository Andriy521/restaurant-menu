from django.contrib.auth.forms import UserCreationForm
from menu.models import Cook


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Cook
        fields = UserCreationForm.Meta.fields + ("years_of_experience",)
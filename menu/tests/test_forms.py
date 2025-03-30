from django.test import TestCase

from menu.forms import UserCreationForm, CookCreationForm


class FormsTests(TestCase):
    def test_cook_creation_form_with_years_of_experience_first_and_lsat_names(self):
        form_data = {
            "username": "new_user",
            "password1": "TEST123User",
            "password2": "TEST123User",
            "first_name": "first",
            "last_name": "last",
            "years_of_experience": 10,
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
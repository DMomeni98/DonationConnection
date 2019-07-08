from django import forms
from charity.models import Charity


class Charity_form(forms.ModelForm):

    class Meta:
        model = Charity
        fields = ['name', 'email', 'password', 'address', 'phone_number', 'post_code']
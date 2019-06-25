from django import forms
from accounts.models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['email', 'username', 'first_name', 'last_name', 'national_id', 'post_code', 'password', 'address']

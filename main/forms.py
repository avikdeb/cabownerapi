from django import forms
from . import models


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = models.manufacturerRegistration
        fields = "__all__"


class LoginForm(forms.Form):
    username_email = forms.CharField(required=True)
    user_password = forms.CharField(required=True)


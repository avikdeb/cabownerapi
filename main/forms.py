from django import forms
from . import models


class RegistrationCarForm(forms.ModelForm):
    class Meta:
        model = models.manufacturerRegistration
        fields = "__all__"


class RegistrationOwnerForm(forms.ModelForm):
    class Meta:
        model = models.ownerRegistration
        fields = "__all__"


class CheckLicenseNumberForm(forms.ModelForm):
    class Meta:
        model = models.manufacturerRegistration
        fields = ["license_number"]


class LoginForm(forms.Form):
    username_email = forms.CharField(required=True)
    user_password = forms.CharField(required=True)


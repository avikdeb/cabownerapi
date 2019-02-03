from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models, forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseForbidden, HttpResponse


class SignUpView(CreateView):
    template_name = "registration/signup.html"
    model = models.User
    success_url = "/logout/"
    form_class = UserCreationForm


class LoginView(FormView):
    template_name = "registration/login.html"
    form_class = forms.LoginForm
    success_url = "/"

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect("/")

        username_email = form.cleaned_data.get("username_email", None)
        password = form.cleaned_data.get("user_password", None)

        if username_email is None or password is None:
            return super(LoginView, self).form_invalid(form)

        user_obj = User.objects.filter(email=username_email).first()
        entry = "email"

        if user_obj is None:
            user_obj = User.objects.filter(username=username_email).first()
            entry = "username"

        if user_obj is None:
            return super(LoginView, self).form_invalid(form)

        else:
            if entry == "email":
                user_auth = authenticate(email=username_email, password=password)

            if entry == "username":
                user_auth = authenticate(username=username_email, password=password)

            if user_auth is None:
                return super(LoginView, self).form_invalid(form)

            login(self.request, user_auth)
        return super(LoginView, self).form_valid(form)
    
    def form_invalid(self, form):
        print(form.errors)
        return super(LoginView, self).form_invalid(form)


class RegisterView(FormView):
    template_name = "register.html"
    form_class = forms.RegistrationForm
    success_url = "/"

    def form_valid(self, form):
        try:
            models.manufacturerRegistration.objects.create(
                license_number=form.cleaned_data.get("license_number", None),
                manufacturing_date=form.cleaned_data.get("manufacturing_date", None),
                manufacturer_name=form.cleaned_data.get("manufacturer_name", None),
                fuel_type=form.cleaned_data.get("fuel_type", None),
                vehicle_color=form.cleaned_data.get("vehicle_color", None),
                vehicle_type=form.cleaned_data.get("vehicle_type", None),
                km_run=form.cleaned_data.get("km_run", None),
                model=form.cleaned_data.get("model", None),
                test1=form.cleaned_data.get("test1", None),
                test2=form.cleaned_data.get("test2", None),
                test3=form.cleaned_data.get("test3", None),
                test4=form.cleaned_data.get("test4", None)
            )
            messages.add_message(self.request, 25, "Form has been submitted successfully.")
        except Exception as e:
            print("Exception: ", e)
            messages.add_message(self.request, 25, "Form submission unsuccessful")
            return super(RegisterView, self).form_invalid(form)

        return super(RegisterView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.add_message(self.request, 25, "Please correct the errors and try again!")
        return super(RegisterView, self).form_invalid(form)

    def get_models(self):

        return models.carModel.objects.all()

    def get_vehicle_types(self):
        return models.carType.objects.all()


class HomeView(TemplateView):
    template_name = "home.html"


def store_logout(request):
    logout(request)
    return HttpResponseRedirect("/")



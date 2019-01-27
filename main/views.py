from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseForbidden, HttpResponse


class SignUpView(CreateView):
    template_name = "registration/signup.html"
    model = models.User
    success_url = "/logout/"
    form_class = UserCreationForm


class RegisterView(TemplateView):
    template_name = "register.html"
    success_url = "/logout/"


class HomeView(TemplateView):
    template_name = "home.html"


def store_logout(request):
    logout(request)
    return HttpResponseRedirect("/")



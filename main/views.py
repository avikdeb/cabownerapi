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
            messages.add_message(self.request, 25, "You already logged in")
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
            messages.add_message(self.request, 25, "You have been logged in successfully")
        return super(LoginView, self).form_valid(form)
    
    def form_invalid(self, form):
        print(form.errors)
        messages.add_message(self.request, 25, "Form invalid, Please try again")
        return super(LoginView, self).form_invalid(form)


class RegisterOwnerView(FormView):
    template_name = "registerOwner.html"
    form_class = forms.RegistrationOwnerForm
    success_url = "/"

    def form_valid(self, form):
        try:
            manufacturer__registration = models.manufacturerRegistration.objects.filter(id=self.kwargs['car_id']).first()
            if manufacturer__registration:
                models.ownerRegistration.objects.create(manufacturer=manufacturer__registration,
                                                        name=form.cleaned_data.get("name", None),
                                                        mobileNumber=form.cleaned_data.get("mobileNumber", None),
                                                        licenseNumber=form.cleaned_data.get("licenseNumber", None),
                                                        dateOfBirth=form.cleaned_data.get("dateOfBirth", None),
                                                        aadharCardFront=form.cleaned_data.get("aadharCardFront", None),
                                                        aadharCardBack=form.cleaned_data.get("aadharCardBack", None),
                                                        licenseFront=form.cleaned_data.get("licenseFront", None),
                                                        licenseBack=form.cleaned_data.get("licenseBack", None),
                                                        photo=form.cleaned_data.get("photo", None),
                                                        addressProof=form.cleaned_data.get("addressProof", None),
                                                        normsAccepted=True)
                messages.add_message(self.request, 25, "Driver has been registered successfully.")

            else:
                messages.add_message(self.request, 25, "Car with License number not found.")
        except Exception as e:
            print("Exception: ", e)
            messages.add_message(self.request, 25, "Form submission unsuccessful")
            return super(RegisterOwnerView, self).form_invalid(form)
        return super(RegisterOwnerView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.add_message(self.request, 25, "Please correct the errors and try again!")
        return super(RegisterOwnerView, self).form_invalid(form)

    def get_manufacturer(self):
        return models.manufacturerRegistration.objects.filter(id=self.kwargs['car_id']).first()


class RegisterCarView(FormView):
    template_name = "register.html"
    form_class = forms.RegistrationCarForm

    def get_car(self):
        return models.manufacturerRegistration.objects.filter(id=self.kwargs['car_id']).first()

    def form_valid(self, form):
        try:
            manufacturer__registration = models.manufacturerRegistration.objects.filter(id=self.kwargs['car_id']).first()
            if manufacturer__registration:
                manufacturer__registration.manufacturing_date = form.cleaned_data.get("manufacturing_date", None)
                manufacturer__registration.manufacturer = form.cleaned_data.get("manufacturer", None)
                manufacturer__registration.fuel_type = form.cleaned_data.get("fuel_type", None)
                manufacturer__registration.rateList = form.cleaned_data.get("rateList", None)
                manufacturer__registration.vehicle_color = form.cleaned_data.get("vehicle_color", None)
                manufacturer__registration.vehicle_type = form.cleaned_data.get("vehicle_type", None)
                manufacturer__registration.km_run = form.cleaned_data.get("km_run", None)
                manufacturer__registration.model = form.cleaned_data.get("model", None)
                manufacturer__registration.rc = form.cleaned_data.get("rc", None)
                manufacturer__registration.fitness = form.cleaned_data.get("fitness", None)
                manufacturer__registration.permit = form.cleaned_data.get("permit", None)
                manufacturer__registration.insurance = form.cleaned_data.get("insurance", None)
                manufacturer__registration.pollution = form.cleaned_data.get("pollution", None)

                messages.add_message(self.request, 25, "Car has been registered successfully.")
                return HttpResponseRedirect("/registerOwner/" + str(manufacturer__registration.id))

            else:
                messages.add_message(self.request, 25, "Car with License number not found.")
        except Exception as e:
            print("Exception: ", e)
            messages.add_message(self.request, 25, "Form submission unsuccessful")
            return super(RegisterCarView, self).form_invalid(form)
        return super(RegisterCarView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.add_message(self.request, 25, "Please correct the errors and try again!")
        return super(RegisterCarView, self).form_invalid(form)

    def get_models(self):
        return models.carModel.objects.all()

    def get_manufacturers(self):
        return models.manufacturer.objects.all()

    def get_vehicleColour(self):
        return models.vehicleColour.objects.all()

    def get_fuelType(self):
        return models.fuelType.objects.all()

    def get_rateList(self):
        return models.rateList.objects.all()

    def get_vehicle_types(self):
        return models.carType.objects.all()


class HomeView(TemplateView):
    template_name = "home.html"


def store_logout(request):
    logout(request)
    return HttpResponseRedirect("/")


class CheckLicenseNumberView(FormView):
    template_name = "checkLicenseNumber.html"
    form_class = forms.CheckLicenseNumberForm
    success_url = "/"

    def get(self, request, *args, **kwargs):
        if self.request.GET.get("action"):
            from models import manufacturerRegistration
            manufacturer__registration = manufacturerRegistration.objects.filter(license_number=self.request.GET.
                                                                                 get("license_number")).first()
            if manufacturer__registration:
                return JsonResponse(
                    {"registered": True})
            else:
                return JsonResponse(
                    {"registered": False})
        else:
            return super(CheckLicenseNumberView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        from models import manufacturerRegistration
        print(self.request.POST.get("license_number"))
        manufacturer__registration = manufacturerRegistration.objects.create(license_number=self.request.POST.get("license_number"))
        # return HttpResponseRedirect("/registerCar/" + str(manufacturer__registration.id))
        return JsonResponse(
            {"car_id": str(manufacturer__registration.id)})



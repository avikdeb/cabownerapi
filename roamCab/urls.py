from django.conf.urls import url, include
from django.contrib import admin
from main import views

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^signup/', views.SignUpView.as_view(), name="signup"),
    url(r'^user/login/', views.LoginView.as_view(), name="login"),
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^registerCar/(?P<car_id>[\w\d-]+)$', views.RegisterCarView.as_view(), name='registerCar'),
    url(r'^checkLicenseNumber/', views.CheckLicenseNumberView.as_view(), name='checkLicenseNumber'),
    url(r'^registerOwner/(?P<car_id>[\w\d-]+)$', views.RegisterOwnerView.as_view(), name='registerOwner'),
]
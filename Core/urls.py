from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name='home'),  # Home page (login required)
    path("signup/", views.authView, name="signup"),  # Registration page
    path("accounts/", include("django.contrib.auth.urls")),  # Login, logout, password reset, etc.
    path('logout/',views.logoutview,name='logout'),
    path('welcome/',views.welcome,name='welcome')
    ]

from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("", views.home, name='home'),  # Home page (login required)
    path("signup/", views.authView, name="signup"),  # Registration page
    path("accounts/", include("django.contrib.auth.urls")),  # Login, logout, password reset, etc.
    path('logout/', LogoutView.as_view(), {'next_page': 'login'}, name='logout'),
    ]

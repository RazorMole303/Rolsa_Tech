from django.urls import path

from .views import CustomLogoutView, CustomLoginView
from . import views


urlpatterns = [
    path('', views.home, name=""),
    path("login", CustomLoginView.as_view(), name="login"),
    path("logout", CustomLogoutView.as_view(), name="logout"),
    path('about/', views.about, name="about"),
    path('register/', views.register, name="register"),
    path('calculator/', views.calculator, name="calculator")
]

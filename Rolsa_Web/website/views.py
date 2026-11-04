from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.views import LogoutView, LoginView
# Create your views here.
def home(request):
    return render(request, 'webpages/home.html')

def about(request):
    return render(request, 'webpages/about.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('')
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account is ready. Please sign in.")
            return redirect("login")
    else:
        form = RegistrationForm()
    return render(request, "registration/register.html", {"form": form})


class CustomLogoutView(LogoutView):
    def post(self,request, *args, **kuargs):
        messages.success(request, "You have succesffuly logged out")
        return super().post(request, *args, **kuargs)


class CustomLoginView(LoginView):
    def post(self,request, *args, **kuargs):
        messages.success(request, "You have succesfully logged in")
        return super().post(request, *args, **kuargs)
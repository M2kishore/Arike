from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView

from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm

# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, "base.html")


class UserLoginView(LoginView):
    template_name = "login.html"


class UserSignupView(CreateView):
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = "/login"

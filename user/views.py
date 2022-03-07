from re import template
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView

from django.forms import ModelForm

from user.models import Users

# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, "base.html")


class UserLoginForm(ModelForm):
    pass


class UserLoginView(LoginView):
    pass


class UserCreateForm(ModelForm):
    class Meta:
        model = Users
        fields = ("full_name", "role", "email", "phone", "password")


class GenericUserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = "signup.html"
    success_url = "dashboard/"

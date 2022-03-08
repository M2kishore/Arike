from msilib.schema import ListView
from re import template
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from django.forms import ModelForm

# from user.models import User

# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, "base.html")


# class UserLoginForm(ModelForm):
#     class Meta:
#         model = Faculty
#         fields = ("user", "role")


class UserLoginView(LoginView):
    template_name = "login.html"
    success_url = "dashboard/"

    def form_valid(self,form):
        self.object = form.save()

def LoginPostView(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("dashboard/")
        # Redirect to a success page.
        ...
    else:
        return render(request,"login.html")

def LoginView(request):
    return render(request,"login.html")
        # Return an 'invalid login' error message.

    # def get(self,request):
    #     return render(request, "login.html")

    # def post(self,request):
    #     email = request.POST.get("email")
    #     password = request.POST.get("password")
    #     user = Users.objects.get(email=email,password=password)
    #     if user:
    #         return HttpResponseRedirect("dashboard/")
    #     else:
    #         return HttpResponseRedirect("login/")

# class UserCreateForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ["username","email","password1","password2"]


class GenericUserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = "login/"


class GenericDashboardView(CreateView):
    pass
#Admin Views

class GenericCreateFacilityView(CreateView):
    pass
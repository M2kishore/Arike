from msilib.schema import ListView
from re import template
from sre_constants import SUCCESS
from django.forms import ModelForm, TextInput, CharField, PasswordInput
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from user.models import Patient, User
from django.contrib.auth.views import LoginView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import login as auth_login
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
    UsernameField,
)


class HomeView(View):
    def get(self, request):
        return render(request, "base.html")


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = "dashboard/"

class UseUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('full_name','phone','email')

class UserUpdateView()

# class UserLoginForm(AuthenticationForm):
#     username = UsernameField(widget=TextInput(attrs={"autofocus": True}))
#     password = CharField(
#         label=_("Password"),
#         strip=False,
#         widget=PasswordInput(attrs={"autocomplete": "current-password"}),
#     )


class UserLoginView(LoginView):
    template_name = "login.html"


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"


class CreatePatientView(CreateView):
    form_class = PatientForm
    template_name = "patient_create.html"
    success_url = "patients/"


class UpdatePatientView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = "patient_update.html"
    success_url = "patients/"

    def get_queryset(self):
        return Patient.objects.filter(deleted=False, nurse=self.request.user)


class DeletePatientView(DeleteView):
    model = Patient
    template_name = "patient_delete.html"
    success_url = "patients/"


class DetailPatientView(DetailView):
    model = Patient
    template_name = "patient_detail.html"

    def get_queryset(self):
        return Patient.objects.filter(deleted=False, nurse=self.request.user)

from django.views.generic.list import ListView
from re import template
from sre_constants import SUCCESS
from django.forms import EmailField, ModelForm, TextInput, CharField, PasswordInput
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import redirect, render
from django.views import View
from user.user import user_created_email
from user.models import (
    Disease,
    District,
    Facility,
    FamilyDetails,
    LgsBody,
    Patient,
    PatientDisease,
    State,
    Treatment,
    TreatmentNotes,
    User,
    VisitDetails,
    VisitSchedule,
    Ward,
)
from django.contrib.auth.views import LoginView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import login, logout, authenticate
from django import forms
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
    UsernameField,
)
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(View):
    def get(self, request):
        return render(request, "base.html")


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "full_name", "role", "phone"]


class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = "signup.html"
    success_url = "login"

    def form_valid(self, form):
        self.object = form.save()
        user_created_email(self.object).delay()
        return HttpResponseRedirect(self.get_success_url())


class UserLoginForm(forms.Form):
    email = EmailField()
    password = CharField(widget=forms.PasswordInput)


def log_in(request):
    error = False
    if request.user.is_authenticated:
        return redirect("/patient")
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect("login")
            else:
                error = True
    else:
        form = UserLoginForm()

    return render(request, "login.html", {"form": form, "error": error})


# class UserLoginForm(AuthenticationForm):
#     username = UsernameField(widget=TextInput(attrs={"autofocus": True}))
#     password = CharField(
#         label=_("Password"),
#         strip=False,
#         widget=PasswordInput(attrs={"autocomplete": "current-password"}),
#     )


class UserLoginView(LoginView):
    template_name = "login.html"


# Patient Views
class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"


class PatientView(ListView):
    queryset = Patient.objects.all()
    template_name = "patient.html"
    context_objects_name = "patients"

    def get_queryset(self):
        print(self.request.user)
        patients = Patient.objects.filter()
        search_string = self.request.GET.get("search")
        if search_string:
            patients = Patient.filter(full_name__icontains=search_string)
        return patients


class CreatePatientView(CreateView):
    form_class = PatientForm
    template_name = "patient-create.html"
    success_url = "patient/"


class UpdatePatientView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = "patient-update.html"
    success_url = "patients/"

    def get_queryset(self):
        return Patient.objects.filter(deleted=False, nurse=self.request.user)


class DeletePatientView(DeleteView):
    model = Patient
    template_name = "patient-delete.html"
    success_url = "patients/"


class DetailPatientView(DetailView):
    model = Patient
    template_name = "patient-details.html"

    def get_queryset(self):
        return Patient.objects.filter(deleted=False, nurse=self.request.user)


# State View
class StateForm(ModelForm):
    class Meta:
        model = State
        fields = "__all__"


class StateView(ListView):
    queryset = State.objects.all()
    template_name = "state.html"
    context_object_name = "states"


class CreateStateView(CreateView):
    form_class = StateForm
    template_name = "state-create.html"
    success_url = "state/"


class UpdateStateView(UpdateView):
    model = State
    form_class = StateForm
    template_name = "state-update.html"
    success_url = "state/"

    def get_queryset(self):
        return State.objects.all()


class DeleteStateView(DeleteView):
    model = State
    template_name = "state-delete.html"
    success_url = "state/"


class DetailStateView(DetailView):
    model = State
    template_name = "state-details.html"

    def get_queryset(self):
        return State.objects.all()


# District View
class DistrictForm(ModelForm):
    class Meta:
        model = District
        fields = "__all__"


class DistrictView(ListView):
    queryset = District.objects.all()
    template_name = "district.html"
    context_object_name = "districts"


class CreateDistrictView(CreateView):
    form_class = DistrictForm
    template_name = "district-create.html"
    success_url = "district/"


class UpdateDistrictView(UpdateView):
    model = District
    form_class = DistrictForm
    template_name = "district-update.html"
    success_url = "district/"

    def get_queryset(self):
        return District.objects.all()


class DeleteDistrictView(DeleteView):
    model = District
    template_name = "district-delete.html"
    success_url = "district/"


class DetailDistrictView(DetailView):
    model = District
    template_name = "district-details.html"

    def get_queryset(self):
        return District.objects.all()


# LgsBody View
class LgsBodyForm(ModelForm):
    class Meta:
        model = LgsBody
        fields = "__all__"


class LgsBodyView(ListView):
    queryset = LgsBody.objects.all()
    template_name = "lgsbody.html"
    context_object_name = "lgsbodies"


class CreateLgsBodyView(CreateView):
    form_class = LgsBodyForm
    template_name = "lgsbody-create.html"
    success_url = "lgsbody/"


class UpdateLgsBodyView(UpdateView):
    model = LgsBody
    form_class = LgsBodyForm
    template_name = "lgsbody-update.html"
    success_url = "lgsbody/"

    def get_queryset(self):
        return LgsBody.objects.all()


class DeleteLgsBodyView(DeleteView):
    model = LgsBody
    template_name = "lgsbody-delete.html"
    success_url = "lgsbody/"


class DetailLgsBodyView(DetailView):
    model = LgsBody
    template_name = "lgsbody-details.html"

    def get_queryset(self):
        return LgsBody.objects.all()


# Ward View
class WardForm(ModelForm):
    class Meta:
        model = Ward
        fields = "__all__"


class WardView(ListView):
    queryset = Ward.objects.all()
    template_name = "lgsbody.html"
    context_object_name = "lgsbodys"


class CreateWardView(CreateView):
    form_class = WardForm
    template_name = "lgsbody-create.html"
    success_url = "lgsbody/"


class UpdateWardView(UpdateView):
    model = Ward
    form_class = WardForm
    template_name = "ward-update.html"
    success_url = "ward/"

    def get_queryset(self):
        return Ward.objects.all()


class DeleteWardView(DeleteView):
    model = Ward
    template_name = "ward-delete.html"
    success_url = "ward/"


class DetailWardView(DetailView):
    model = Ward
    template_name = "ward-details.html"

    def get_queryset(self):
        return Ward.objects.all()


# Facility
class FacilityForm(ModelForm):
    class Meta:
        model = Facility
        fields = "__all__"


class FacilityView(ListView):
    queryset = Facility.objects.all()
    template_name = "facility.html"
    context_object_name = "facilities"


class CreateFacilityView(CreateView):
    form_class = FacilityForm
    template_name = "facility-create.html"
    success_url = "facility/"


class UpdateFacilityView(UpdateView):
    model = Facility
    form_class = FacilityForm
    template_name = "facility-update.html"
    success_url = "facility/"

    def get_queryset(self):
        return Facility.objects.all()


class DeleteFacilityView(DeleteView):
    model = Facility
    template_name = "facility-delete.html"
    success_url = "facility/"


class DetailFacilityView(DetailView):
    model = Facility
    template_name = "facility-details.html"

    def get_queryset(self):
        return Facility.objects.all()


# Family Details View
class FamilyDetailsForm(ModelForm):
    class Meta:
        model = FamilyDetails
        fields = "__all__"


class FamilyDetailsView(ListView):
    queryset = FamilyDetails.objects.all()
    template_name = "familydetails.html"
    context_object_name = "facilities"


class CreateFamilyDetailsView(CreateView):
    form_class = FamilyDetailsForm
    template_name = "familydetails-create.html"
    success_url = "familydetails/"


class UpdateFamilyDetailsView(UpdateView):
    model = FamilyDetails
    form_class = FamilyDetailsForm
    template_name = "familydetails-update.html"
    success_url = "familydetails/"

    def get_queryset(self):
        return FamilyDetails.objects.all()


class DeleteFamilyDetailsView(DeleteView):
    model = FamilyDetails
    template_name = "familydetails-delete.html"
    success_url = "familydetails/"


class DetailFamilyDetailsView(DetailView):
    model = FamilyDetails
    template_name = "familydetails-details.html"

    def get_queryset(self):
        return FamilyDetails.objects.all()


# Disease
class DiseaseForm(ModelForm):
    class Meta:
        model = Disease
        fields = "__all__"


class DiseaseView(ListView):
    queryset = Disease.objects.all()
    template_name = "disease.html"
    context_object_name = "facilities"


class CreateDiseaseView(CreateView):
    form_class = DiseaseForm
    template_name = "disease-create.html"
    success_url = "disease/"


class UpdateDiseaseView(UpdateView):
    model = Disease
    form_class = DiseaseForm
    template_name = "disease-update.html"
    success_url = "disease/"

    def get_queryset(self):
        return Disease.objects.all()


class DeleteDiseaseView(DeleteView):
    model = Disease
    template_name = "disease-delete.html"
    success_url = "disease/"


class DetailDiseaseView(DetailView):
    model = Disease
    template_name = "disease-details.html"

#Patient Disease
class PatientDiseaseForm(ModelForm):
    class Meta:
        model = PatientDisease
        fields = "__all__"


class PatientDiseaseView(ListView):
    queryset = PatientDisease.objects.all()
    template_name = "patientdisease.html"
    context_object_name = "patientdisease"


class CreatePatientDiseaseView(CreateView):
    form_class = PatientDiseaseForm
    template_name = "patientdisease-create.html"
    success_url = "patientdisease/"


class UpdatePatientDiseaseView(UpdateView):
    model = PatientDisease
    form_class = PatientDiseaseForm
    template_name = "patientdisease-update.html"
    success_url = "patientdisease/"

    def get_queryset(self):
        return PatientDisease.objects.all()


class DeletePatientDiseaseView(DeleteView):
    model = PatientDisease
    template_name = "patientdisease-delete.html"
    success_url = "patientdisease/"


class DetailPatientDiseaseView(DetailView):
    model = PatientDisease
    template_name = "patientdisease-details.html"

#Visit Schedule
class VisitScheduleForm(ModelForm):
    class Meta:
        model = VisitSchedule
        fields = "__all__"


class VisitScheduleView(ListView):
    queryset = VisitSchedule.objects.all()
    template_name = "visitschedule.html"
    context_object_name = "visitschedule"


class CreateVisitScheduleView(CreateView):
    form_class = VisitScheduleForm
    template_name = "visitschedule-create.html"
    success_url = "visitschedule/"


class UpdateVisitScheduleView(UpdateView):
    model = VisitSchedule
    form_class = VisitScheduleForm
    template_name = "visitschedule-update.html"
    success_url = "visitschedule/"

    def get_queryset(self):
        return VisitSchedule.objects.all()


class DeleteVisitScheduleView(DeleteView):
    model = VisitSchedule
    template_name = "visitschedule-delete.html"
    success_url = "visitschedule/"


class DetailVisitScheduleView(DetailView):
    model = VisitSchedule
    template_name = "visitschedule-details.html"

#Visit Details
class VisitDetailsForm(ModelForm):
    class Meta:
        model = VisitDetails
        fields = "__all__"


class VisitDetailsView(ListView):
    queryset = VisitDetails.objects.all()
    template_name = "visitdetails.html"
    context_object_name = "visitdetails"


class CreateVisitDetailsView(CreateView):
    form_class = VisitDetailsForm
    template_name = "visitdetails-create.html"
    success_url = "visitdetails/"


class UpdateVisitDetailsView(UpdateView):
    model = VisitDetails
    form_class = VisitDetailsForm
    template_name = "visitdetails-update.html"
    success_url = "visitdetails/"

    def get_queryset(self):
        return VisitDetails.objects.all()


class DeleteVisitDetailsView(DeleteView):
    model = VisitDetails
    template_name = "visitdetails-delete.html"
    success_url = "visitdetails/"


class DetailVisitDetailsView(DetailView):
    model = VisitDetails
    template_name = "visitdetails-details.html"

#Treatment
class TreatmentForm(ModelForm):
    class Meta:
        model = Treatment
        fields = "__all__"


class TreatmentView(ListView):
    queryset = Treatment.objects.all()
    template_name = "treatment.html"
    context_object_name = "treatment"


class CreateTreatmentView(CreateView):
    form_class = TreatmentForm
    template_name = "treatment-create.html"
    success_url = "treatment/"


class UpdateTreatmentView(UpdateView):
    model = Treatment
    form_class = TreatmentForm
    template_name = "treatment-update.html"
    success_url = "treatment/"

    def get_queryset(self):
        return Treatment.objects.all()


class DeleteTreatmentView(DeleteView):
    model = Treatment
    template_name = "treatment-delete.html"
    success_url = "treatment/"


class DetailTreatmentView(DetailView):
    model = Treatment
    template_name = "treatment-details.html"

#Treatment Notes
class TreatmentNotesForm(ModelForm):
    class Meta:
        model = TreatmentNotes
        fields = "__all__"


class TreatmentNotesView(ListView):
    queryset = TreatmentNotes.objects.all()
    template_name = "treatmentnotes.html"
    context_object_name = "treatmentnotes"


class CreateTreatmentNotesView(CreateView):
    form_class = TreatmentNotesForm
    template_name = "treatmentnotes-create.html"
    success_url = "treatmentnotes/"


class UpdateTreatmentNotesView(UpdateView):
    model = TreatmentNotes
    form_class = TreatmentNotesForm
    template_name = "treatmentnotes-update.html"
    success_url = "treatmentnotes/"

    def get_queryset(self):
        return TreatmentNotes.objects.all()


class DeleteTreatmentNotesView(DeleteView):
    model = TreatmentNotes
    template_name = "treatmentnotes-delete.html"
    success_url = "treatmentnotes/"


class DetailTreatmentNotesView(DetailView):
    model = Treatment
    template_name = "treatment-details.html"
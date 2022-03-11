from pyexpat import model
from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
# Create your models here.

LOCAL_BODY_CHOICES = (
    # Panchayath levels
    (1, "Grama Panchayath"),
    (2, "Block Panchayath"),
    (3, "District Panchayath"),
    (4, "Nagar Panchayath"),
    # Municipality levels
    (10, "Municipality"),
    # Corporation levels
    (20, "Corporation"),
    # Unknown
    (50, "Others"),
)


class State(models.Model):
    name = models.CharField(max_length=255)


class District(models.Model):
    name = models.CharField(max_length=255)
    state = models.ForeignKey("State", on_delete=models.PROTECT)


class LgsBody(models.Model):
    name = models.CharField(max_length=100)
    kind = models.CharField(
        max_length=100, choices=LOCAL_BODY_CHOICES, default=LOCAL_BODY_CHOICES[0][0]
    )
    lgs_body_code = models.CharField(max_length=20, blank=True, null=True)

    district = models.ForeignKey("District", on_delete=models.PROTECT)


class Ward(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    lgs_body = models.ForeignKey("LgsBody", on_delete=models.PROTECT)


FACILITY_KIND_CHOICES = (
    ("PHC", "PHC"),
    ("CHC", "CHC"),
)


class Facility(models.Model):
    kind = models.CharField(
        max_length=10,
        choices=FACILITY_KIND_CHOICES,
        default=FACILITY_KIND_CHOICES[0][0],
    )
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    pincode = models.IntegerField()
    phone = models.IntegerField()
    ward = models.ForeignKey("Ward", on_delete=models.PROTECT, null=True, blank=True)


USERS_ROLE_CHOICES = (
    ("primary_nurse", "primary_nurse"),
    ("secondary_nurse", "secondary_nurse"),
    ("district_admin", "district_admin"),
)

class AccountManager(BaseUserManager):
    def create_user(self,email,full_name,role,phone,password,**other_fields):
        
        if not email:
            raise ValueError(_("Enter email address"))

        email = self.normalize_email(email)
        user = self.model(email=email,full_name=full_name,role=role,phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,full_name,role,phone,password,**other_fields):
        user = self.create_user(email,full_name,"district_admin",phone,password,**other_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    full_name = models.CharField(max_length=100)
    role = models.CharField(
        max_length=15,
        choices=USERS_ROLE_CHOICES,
        default=USERS_ROLE_CHOICES[0][0],
    )
    phone = models.IntegerField(unique=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    #objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name','role','phone']


GENDER_CHOICES = (("Male", "Male"), ("Female", "Female"), (3, "Non_Binary"))


class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(default=datetime.date.today())
    address = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255)
    phone = models.IntegerField()
    gender = models.CharField(
        max_length=100,
        choices=GENDER_CHOICES,
        default=GENDER_CHOICES[0][0],
    )
    emergency_phone_number = models.IntegerField()
    expired_time = models.DateTimeField(null=True,default = timezone.now())
    ward = models.ForeignKey("Ward", on_delete=models.PROTECT, null=True, blank=True)


RELATION_CHOICES = (
    ("OTHER", "OTHER"),
    ("BROTHER", "BROTHER"),
    ("FATHER", "FATHER"),
    ("MOTHER", "MOTHER"),
    ("SON", "SON"),
    ("DAUGHTER", "DAUGHTER"),
    ("GRAND_FATHER", "GRAND_FATHER"),
    ("GRAND_MOTHER", "GRAND_MOTHER"),
    ("GUARDIAN", "GURDIAN"),
)


class FamilyDetails(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    date_of_birth = models.DateField()
    email = models.EmailField(max_length=100)
    relation = models.CharField(
        max_length=100,
        choices=RELATION_CHOICES,
        default=RELATION_CHOICES[0][0],
    )
    address = models.CharField(max_length=255)
    education = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    remarks = models.CharField(max_length=255)
    is_primary = models.BooleanField(default=False)
    patient = models.ForeignKey("Patient", on_delete=models.PROTECT)


ICDS_CODE_CHOICES = (
    ("D-32", "DM"),
    ("HT-58", "Hypertension"),
    ("IHD-21", "IDH"),
    ("DPOC-144", "COPD"),
    ("DM-62", "Dementia"),
    ("CVA-89", "CVA"),
    ("C-98", "Cancer"),
    ("DC-225", "CKD"),
)


class Disease(models.Model):
    name = models.CharField(max_length=100)
    icds_code = models.CharField(
        max_length=100, choices=ICDS_CODE_CHOICES, default=ICDS_CODE_CHOICES[0][0]
    )


class PatientDisease(models.Model):
    patient = models.ForeignKey("Patient", on_delete=models.PROTECT)
    disease = models.ForeignKey("Disease", on_delete=models.PROTECT)
    note = models.CharField(max_length=255)


class VisitSchedule(models.Model):
    date = models.DateTimeField()
    # minutes
    duration = models.IntegerField()
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)
    nurse = models.ForeignKey(User, on_delete=models.PROTECT)


PALLIVATIVE_PHASE_CHOICES = (
    ("STABLE", "STABLE"),
    ("UNSTABLE", "USTABLE"),
    ("DETORIATING", "DETORIATING"),
    ("TERMINAL", "TERMINAL"),
    ("BEREAVEMENT", "BEREAVEMENT"),
)
SYMPTOMS_CHOICES = (
    ("NONE", "NONE"),
    ("HEADACHE", "HEADACHE"),
    ("STOMACHACHE", "STOMACHACHE"),
    ("VOMITING", "VOMITING"),
    ("CHESTPAIN", "CHESTPAIN"),
)


class VisitDetails(models.Model):
    pallivative_phase = models.CharField(
        max_length=100,
        choices=PALLIVATIVE_PHASE_CHOICES,
        default=PALLIVATIVE_PHASE_CHOICES[0][0],
    )
    blood_pressure = models.IntegerField()
    pulse = models.IntegerField()
    general_random_blood_sugar = models.IntegerField()
    personal_hygine = models.CharField(max_length=10)
    mouth_hygine = models.CharField(max_length=100)
    public_hygine = models.CharField(max_length=100)
    systemic_examination = models.CharField(max_length=100)
    patient_at_peace = models.BooleanField(default=True)
    pain = models.BooleanField(default=True)
    symptoms = models.CharField(
        max_length=100, choices=SYMPTOMS_CHOICES, default=SYMPTOMS_CHOICES[0][0]
    )
    note = note = models.CharField(max_length=255)
    visit_schedule = models.ForeignKey("VisitSchedule", on_delete=models.PROTECT)


TREATMENT_CHOICES = (
    ("GENERAL_CARE", "GENERAL_CARE"),
    ("GENITO_URINARY_CARE", "GENITO_URINARY_CARE"),
    ("GASTRO_INTESTINAL_CARE", "GASTRO_INTESTINAL_CARE"),
    ("WOUND_CARE", "WOUND_CARE"),
    ("RESPIRATORY_CARE", "RESPIRATORY_CARE"),
)


class Treatment(models.Model):
    description = models.CharField(max_length=255)
    care_type = models.CharField(
        max_length=100, choices=TREATMENT_CHOICES, default=TREATMENT_CHOICES[0][0]
    )
    patient = models.ForeignKey("Patient", on_delete=models.PROTECT)


class TreatmentNotes(models.Model):
    note = models.CharField(max_length=255)
    describe = models.CharField(max_length=255)
    visit = models.ForeignKey("VisitDetails", on_delete=models.PROTECT)
    treatment = models.ForeignKey("Treatment", on_delete=models.PROTECT)

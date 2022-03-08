from django.contrib import admin
from user.models import User

# Register your models here.
admin.sites.site.register(User)
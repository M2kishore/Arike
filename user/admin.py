from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User,State,District,LgsBody,Ward,Disease,Facility

class FacilityAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Facility._meta.fields]
    search_fields = ('name','ward')

    filter_horizontal = ()
    list_flter = ()
    fieldset = ()
# Register your models here.
admin.sites.site.register(User)
admin.sites.site.register(State)
admin.sites.site.register(LgsBody)
admin.sites.site.register(District)
admin.sites.site.register(Ward)
admin.sites.site.register(Disease)
admin.sites.site.register(Facility, FacilityAdmin)
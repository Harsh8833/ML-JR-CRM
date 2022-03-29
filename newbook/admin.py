from django.contrib import admin
from newbook.models import booking
from django.contrib.admin.sites import site
class ServiceAdmin(admin.ModelAdmin):
    list_display=('id', 'cname', 'phone', 'form', 'aadhar', 'pan')
admin.site.register(booking,ServiceAdmin)
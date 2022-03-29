from django.contrib import admin
from newbook.models import booking
from django.contrib.admin.sites import site
class ServiceAdmin(admin.ModelAdmin):
    list_display=('cname', 'phone', 'id')
admin.site.register(booking,ServiceAdmin)
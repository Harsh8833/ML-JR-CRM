from django.contrib import admin
from newbooking.models import new_booking
from django.contrib.admin.sites import site

class ServiceAdmin(admin.ModelAdmin):
    list_display=('booking_id', 'cname', 'phone', 'form', 'aadhar', 'pan')
admin.site.register(new_booking,ServiceAdmin)
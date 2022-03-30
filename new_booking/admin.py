from django.contrib import admin
from new_booking.models import newbooking
from django.contrib.admin.sites import site



class ServiceAdmin(admin.ModelAdmin):
    list_display=('booking_id', 'cname', 'phone', 'form', 'aadhar', 'pan')
admin.site.register(newbooking,ServiceAdmin)
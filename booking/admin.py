from django.contrib import admin
from booking.models import newBooking
from django.contrib.admin.sites import site



class ServiceAdmin(admin.ModelAdmin):
    list_display=('booking_id', 'cname', 'phone', 'form', 'aadhar', 'pan')
admin.site.register(newBooking,ServiceAdmin)
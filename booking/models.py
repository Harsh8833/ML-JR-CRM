from django.db import models

# Create your models here.
class newBooking(models.Model):
    cname = models.CharField(max_length=50, blank=False)
    phone = models.IntegerField(blank=False)
    form = models.FileField( upload_to="files", blank=False, null= False)
    pan = models.FileField( upload_to="files", blank=False, null=False)
    aadhar = models.FileField(upload_to="files", blank=False , null=False)
    booking_id = models.AutoField(primary_key=True)
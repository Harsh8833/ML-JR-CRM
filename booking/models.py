from django.db import models

# Create your models here.
class newBooking(models.Model):
    cname = models.CharField(max_length=50, blank=False)
    phone = models.IntegerField(blank=False)
    form = models.FileField( upload_to="files/%Y/%m/%d/", blank=False)
    pan = models.FileField( upload_to="files/%Y/%m/%d/", blank=False)
    aadhar = models.FileField(upload_to="files/%Y/%m/%d/", blank=False)
    booking_id = models.AutoField(primary_key=True)
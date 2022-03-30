from django.db import models

# Create your models here.
class newbooking(models.Model):
    cname = models.CharField(max_length=50)
    phone = models.IntegerField()
    form = models.FileField( upload_to="files", blank=True)
    pan = models.FileField( upload_to="files", blank=True)
    aadhar = models.FileField(upload_to="files", blank=True)
    booking_id = models.AutoField(primary_key=True)
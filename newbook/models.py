from django.db import models

# Create your models here.
class booking(models.Model):
    cname=models.CharField(max_length=50)
    phone=models.IntegerField()
    pan=models.FileField( upload_to="files", blank=True)
    id=models.AutoField(primary_key=True)
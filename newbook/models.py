from django.db import models

# Create your models here.
class booking(models.Model):
    cname=models.CharField(max_length=50)
    phone=models.IntegerField()
    
    id=models.AutoField(primary_key=True)
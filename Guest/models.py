from django.db import models
from Admin.models import tbl_place
# Create your models here.

class tbl_user(models.Model):
    user_place= models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    user_name=  models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_contact = models.CharField(max_length=50)
    user_photo = models.FileField(upload_to='Assets/Files/User')

class tbl_travelagency(models.Model):
    agency_place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    agency_name=  models.CharField(max_length=50)
    agency_email = models.CharField(max_length=50)
    agency_contact = models.CharField(max_length=50)
    agency_address = models.CharField(max_length=50)
    agency_photo = models.FileField(upload_to='Assets/Files/User')
    agency_license = models.FileField(upload_to='Assets/Files/User')
    agency_password = models.CharField(max_length=50)
    agency_status = models.IntegerField(default=0)
from django.db import models
from Admin.models import *
from Guest.models import *

# Create your models here.

class tbl_package(models.Model):
    package_name = models.CharField(max_length=100)
    package_price = models.CharField(max_length=100)
    package_details = models.CharField(max_length=1000)
    package_type_id = models.ForeignKey(tbl_package_type, on_delete=models.CASCADE)
    agency = models.ForeignKey(tbl_travelagency,on_delete=models.CASCADE)

class tbl_packagelocation(models.Model):
    package_id = models.ForeignKey(tbl_package, on_delete=models.CASCADE)
    location_id = models.ForeignKey(tbl_location,on_delete=models.CASCADE)

class tbl_agencycomplaint(models.Model):
    complaint_date=models.DateField(auto_now_add=True)
    complaint_content=models.CharField(max_length=500)
    complaint_status=models.IntegerField(default=0)
    complaint_reply=models.CharField(max_length=500)
    agency_id=models.ForeignKey(tbl_travelagency,on_delete=models.CASCADE)

class tbl_agencyfeedback(models.Model):
    feedback_content=models.CharField(max_length=500)
    feedback_date=models.DateField(auto_now=True)
    agency_id=models.ForeignKey(tbl_travelagency,on_delete=models.CASCADE)
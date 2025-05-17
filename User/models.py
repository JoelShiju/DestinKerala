from django.db import models
from Guest.models import *
from Admin.models import *
from TravelAgency.models import *

# Create your models here.

class  tbl_packagebooking(models.Model):
    packagebooking_status=models.IntegerField(default=0)
    packagebooking_date=models.DateField(auto_now=True)
    packagebooking_fordate=models.DateField()
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    packagelocation_id=models.ForeignKey(tbl_packagelocation,on_delete=models.CASCADE)
    person_count=models.IntegerField(default=0)

class tbl_complaint(models.Model):
    complaint_date=models.DateField(auto_now_add=True)
    complaint_content=models.CharField(max_length=500)
    complaint_status=models.IntegerField(default=0)
    complaint_reply=models.CharField(max_length=500)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    agency_id=models.ForeignKey(tbl_travelagency,on_delete=models.CASCADE)

class tbl_rating(models.Model):
    rating_content=models.CharField(max_length=500)
    rating_value=models.IntegerField()
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    agency_id=models.ForeignKey(tbl_travelagency,on_delete=models.CASCADE)
    rating_datetime=models.DateTimeField(auto_now=True)

class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=500)
    feedback_date=models.DateField(auto_now=True)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_locationreview(models.Model):
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    location = models.ForeignKey(tbl_location, on_delete=models.CASCADE)
    location_date = models.DateField(auto_now_add=True)
    location_review = models.CharField(max_length=500)
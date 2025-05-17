from django.db import models

# Create your models here.

class tbl_district(models.Model):
    district_name = models.CharField(max_length=30)

class tbl_category(models.Model):
    category_name = models.CharField(max_length=30)

class tbl_adminregistration(models.Model):
    admin_name =  models.CharField(max_length=30)
    admin_email = models.CharField(max_length=30)
    admin_password = models.CharField(max_length=30)


class tbl_place(models.Model):
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)
    place_name=models.CharField(max_length=50)

class tbl_subcategory(models.Model):
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)
    subcategory_name=models.CharField(max_length=50)

class tbl_location(models.Model):
    place_id=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    location_name=models.CharField(max_length=50)
    location_photo=models.FileField(upload_to='Assets/Files/User')

class tbl_location_gallery(models.Model):
    gallery_caption=models.CharField(max_length=500)
    gallery_file=models.FileField(upload_to='Assets/Files/User')
    location=models.ForeignKey(tbl_location,on_delete=models.CASCADE)

class tbl_package_type(models.Model):
    package_type_name=models.CharField(max_length=50)
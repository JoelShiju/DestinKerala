# Generated by Django 5.1.3 on 2025-01-17 08:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0008_tbl_package_type'),
        ('Guest', '0010_delete_tbl_travelagency'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_travelagency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency_name', models.CharField(max_length=50)),
                ('agency_email', models.CharField(max_length=50)),
                ('agency_contact', models.CharField(max_length=50)),
                ('agency_address', models.CharField(max_length=50)),
                ('agency_photo', models.FileField(upload_to='Assets/Files/User')),
                ('agency_license', models.FileField(upload_to='Assets/Files/User')),
                ('agency_password', models.CharField(max_length=50)),
                ('agency_status', models.IntegerField(default=0)),
                ('agency_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
    ]

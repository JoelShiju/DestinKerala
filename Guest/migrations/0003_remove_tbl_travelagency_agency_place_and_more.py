# Generated by Django 5.1.3 on 2025-01-09 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0002_alter_tbl_registration_photo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_travelagency',
            name='agency_place',
        ),
        migrations.DeleteModel(
            name='tbl_registration',
        ),
        migrations.DeleteModel(
            name='tbl_travelagency',
        ),
    ]

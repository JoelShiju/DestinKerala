# Generated by Django 5.1.3 on 2025-03-03 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TravelAgency', '0004_tbl_agencyfeedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_agencycomplaint',
            name='complaint_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]

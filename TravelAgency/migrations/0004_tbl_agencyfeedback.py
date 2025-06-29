# Generated by Django 5.1.3 on 2025-02-14 05:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0011_tbl_travelagency'),
        ('TravelAgency', '0003_tbl_agencycomplaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_agencyfeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_content', models.CharField(max_length=500)),
                ('feedback_date', models.DateField(auto_now=True)),
                ('agency_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_travelagency')),
            ],
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-20 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_and_site_settings', '0003_rename_licenseplates_licenseplate_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LicensePlate',
            new_name='LicensePlateList',
        ),
    ]
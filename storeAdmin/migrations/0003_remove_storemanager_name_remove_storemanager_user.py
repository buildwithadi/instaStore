# Generated by Django 4.2.20 on 2025-07-14 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("storeAdmin", "0002_remove_storemanager_email_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="storemanager",
            name="name",
        ),
        migrations.RemoveField(
            model_name="storemanager",
            name="user",
        ),
    ]

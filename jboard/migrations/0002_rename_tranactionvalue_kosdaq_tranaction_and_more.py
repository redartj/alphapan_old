# Generated by Django 4.1.2 on 2023-01-08 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("jboard", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="kosdaq",
            old_name="tranactionvalue",
            new_name="tranaction",
        ),
        migrations.RenameField(
            model_name="kospi",
            old_name="tranactionvalue",
            new_name="tranaction",
        ),
    ]

# Generated by Django 4.0.6 on 2022-08-17 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ZumaApp', '0003_alter_index_upload'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='username',
            new_name='email_address',
        ),
    ]

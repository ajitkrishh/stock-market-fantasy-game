# Generated by Django 3.1.1 on 2020-11-28 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20201128_2320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='winner',
            old_name='contest_id',
            new_name='contest',
        ),
    ]

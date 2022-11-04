# Generated by Django 3.1.1 on 2020-12-09 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_auto_20201206_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='referal_id',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='extendeduser',
            name='refereal_used',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='extendeduser',
            name='total_referals',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
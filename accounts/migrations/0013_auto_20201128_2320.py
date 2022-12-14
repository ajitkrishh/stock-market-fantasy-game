# Generated by Django 3.1.1 on 2020-11-28 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_checkall_is_allchecked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contestjoinedbyuser',
            name='winner',
        ),
        migrations.CreateModel(
            name='winner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('contest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.contestjoinedbyuser')),
                ('winner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='accounts.userprofile')),
            ],
        ),
    ]

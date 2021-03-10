# Generated by Django 3.1.5 on 2021-03-06 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProxy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestampAdded', models.DateTimeField(default=django.utils.timezone.now)),
                ('timestampUpdated', models.DateTimeField(default=django.utils.timezone.now)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('protokol', models.CharField(blank=True, default='High', max_length=6)),
                ('country', models.CharField(blank=True, default='DE', max_length=10)),
                ('onlineStatus', models.BooleanField(default=False)),
                ('anonymitaetsLevel', models.CharField(blank=True, default='High', max_length=14)),
                ('latenz', models.FloatField(blank=True)),
                ('speed', models.IntegerField(blank=True)),
                ('ipAdress', models.GenericIPAddressField(default='0.0.0.0')),
                ('port', models.IntegerField(blank=True, default=8080)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
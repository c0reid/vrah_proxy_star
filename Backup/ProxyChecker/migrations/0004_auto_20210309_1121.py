# Generated by Django 3.1.5 on 2021-03-09 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ProxyChecker', '0003_auto_20210307_2340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userproxy',
            old_name='timestampUpdated',
            new_name='timestampChecked',
        ),
        migrations.AlterField(
            model_name='userproxy',
            name='ipAdress',
            field=models.GenericIPAddressField(default=''),
        ),
        migrations.AlterField(
            model_name='userproxy',
            name='port',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='userproxy',
            name='protokol',
            field=models.CharField(blank=True, max_length=16),
        ),
        migrations.CreateModel(
            name='LoadedPrxy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestampAdded', models.DateTimeField(default=django.utils.timezone.now)),
                ('timestampChecked', models.DateTimeField(default=django.utils.timezone.now)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('protokol', models.CharField(blank=True, max_length=16)),
                ('country', models.CharField(blank=True, default='DE', max_length=20)),
                ('countryCode', models.CharField(blank=True, default='DE', max_length=2)),
                ('onlineStatus', models.BooleanField(default=False)),
                ('anonymitaetsLevel', models.CharField(blank=True, default='High', max_length=14)),
                ('latenz', models.FloatField(blank=True)),
                ('speed', models.IntegerField(blank=True)),
                ('ipAdress', models.GenericIPAddressField(default='')),
                ('port', models.IntegerField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GoodProxy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestampAdded', models.DateTimeField(default=django.utils.timezone.now)),
                ('timestampChecked', models.DateTimeField(default=django.utils.timezone.now)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('protokol', models.CharField(blank=True, max_length=16)),
                ('country', models.CharField(blank=True, default='DE', max_length=20)),
                ('countryCode', models.CharField(blank=True, default='DE', max_length=2)),
                ('onlineStatus', models.BooleanField(default=False)),
                ('anonymitaetsLevel', models.CharField(blank=True, default='High', max_length=14)),
                ('latenz', models.FloatField(blank=True)),
                ('speed', models.IntegerField(blank=True)),
                ('ipAdress', models.GenericIPAddressField(default='')),
                ('port', models.IntegerField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BadProxy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestampAdded', models.DateTimeField(default=django.utils.timezone.now)),
                ('timestampChecked', models.DateTimeField(default=django.utils.timezone.now)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('protokol', models.CharField(blank=True, max_length=16)),
                ('country', models.CharField(blank=True, default='DE', max_length=20)),
                ('countryCode', models.CharField(blank=True, default='DE', max_length=2)),
                ('onlineStatus', models.BooleanField(default=False)),
                ('anonymitaetsLevel', models.CharField(blank=True, default='High', max_length=14)),
                ('latenz', models.FloatField(blank=True)),
                ('speed', models.IntegerField(blank=True)),
                ('ipAdress', models.GenericIPAddressField(default='')),
                ('port', models.IntegerField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
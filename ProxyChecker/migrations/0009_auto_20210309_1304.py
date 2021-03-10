# Generated by Django 3.1.5 on 2021-03-09 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProxyChecker', '0008_auto_20210309_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badproxy',
            name='anonymitaetsLevel',
            field=models.CharField(blank=True, default='none', max_length=14),
        ),
        migrations.AlterField(
            model_name='badproxy',
            name='country',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='badproxy',
            name='countryCode',
            field=models.CharField(blank=True, default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='badproxy',
            name='port',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='badproxy',
            name='timestampChecked',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='goodproxy',
            name='anonymitaetsLevel',
            field=models.CharField(blank=True, default='none', max_length=14),
        ),
        migrations.AlterField(
            model_name='goodproxy',
            name='ipAdress',
            field=models.GenericIPAddressField(default='0.0.0.0'),
        ),
        migrations.AlterField(
            model_name='loadedprxy',
            name='anonymitaetsLevel',
            field=models.CharField(blank=True, default='none', max_length=14),
        ),
        migrations.AlterField(
            model_name='userproxy',
            name='anonymitaetsLevel',
            field=models.CharField(blank=True, default='none', max_length=14),
        ),
    ]

# Generated by Django 3.1.5 on 2021-03-09 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProxyChecker', '0009_auto_20210309_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badproxy',
            name='timestampChecked',
            field=models.DateTimeField(null=True),
        ),
    ]
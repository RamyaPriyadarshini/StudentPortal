# Generated by Django 2.0.5 on 2019-03-06 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0011_auto_20190306_2000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leave',
            name='leaveType',
        ),
    ]

# Generated by Django 3.2.9 on 2021-11-19 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='user',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='Pet',
        ),
    ]

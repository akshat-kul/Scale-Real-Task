# Generated by Django 3.2.15 on 2022-09-18 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0006_orderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='base_id',
            new_name='base',
        ),
    ]

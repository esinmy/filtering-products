# Generated by Django 2.2.4 on 2020-04-15 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20200412_1427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='user',
            new_name='author',
        ),
    ]

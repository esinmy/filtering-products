# Generated by Django 2.2.4 on 2020-04-11 18:27

from django.db import migrations
import phonenumbers


def prettify_phone_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        phone = phonenumbers.parse(flat.owners_phonenumber, "RU")
        if phonenumbers.is_valid_number(phone):
            flat.owner_phone_pure = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.E164)
            flat.save()


def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.owner_phone_pure = ""
        flat.save()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0007_flat_owner_phone_pure'),
    ]

    operations = [
        migrations.RunPython(prettify_phone_numbers, move_backward),
    ]

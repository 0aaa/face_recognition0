# Generated by Django 4.0.5 on 2022-06-18 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_photo_options_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['name'], 'permissions': (('moderator_required', 'Set user as moderator'),)},
        ),
    ]
# Generated by Django 4.0.5 on 2022-06-13 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.FileField(help_text="Enter a person's photo", upload_to='images_base'),
        ),
    ]
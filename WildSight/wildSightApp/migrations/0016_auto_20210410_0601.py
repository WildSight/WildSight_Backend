# Generated by Django 3.1.7 on 2021-04-10 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wildSightApp', '0015_merge_20210409_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='species',
            name='image',
            field=models.ImageField(blank=True, upload_to='Species_Images/'),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]

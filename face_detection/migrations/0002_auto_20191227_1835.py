# Generated by Django 3.0.1 on 2019-12-27 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("face_detection", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="faceencoding",
            name="album_id",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="faceencoding",
            name="image_id",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-01 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("video", "0002_videolike"),
    ]

    operations = [
        migrations.AlterField(
            model_name="videolike",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
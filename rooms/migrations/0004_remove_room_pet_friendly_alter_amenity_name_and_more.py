# Generated by Django 4.1.4 on 2023-08-12 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0003_alter_room_amenities_alter_room_category_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="room",
            name="pet_friendly",
        ),
        migrations.AlterField(
            model_name="amenity",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="room",
            name="city",
            field=models.CharField(default="Seoul", max_length=50),
        ),
        migrations.AlterField(
            model_name="room",
            name="country",
            field=models.CharField(default="South Korea", max_length=50),
        ),
        migrations.AlterField(
            model_name="room",
            name="kind",
            field=models.CharField(
                choices=[
                    ("entire place", "Entire Place"),
                    ("private room", "Private Room"),
                    ("shared room", "Shared Room"),
                ],
                default="entire place",
                max_length=25,
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]

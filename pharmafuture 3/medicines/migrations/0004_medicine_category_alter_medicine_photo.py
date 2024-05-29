# Generated by Django 4.2.11 on 2024-05-28 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("medicines", "0003_medicine_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="medicine",
            name="category",
            field=models.CharField(
                choices=[
                    ("Antibiotic", "Antibiotic"),
                    ("Anti-Allergic", "Anti-Allergic"),
                    ("Antidepressant", "Antidepressant"),
                    ("Painkiller", "Painkiller"),
                    ("Vitamins", "Vitamins"),
                ],
                default="Vitamins",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="medicine",
            name="photo",
            field=models.ImageField(
                default="medicines/static/img/1.jpg", upload_to="img"
            ),
        ),
    ]
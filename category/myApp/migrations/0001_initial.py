# Generated by Django 4.1.4 on 2022-12-20 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categories",
            fields=[
                (
                    "categoryid",
                    models.IntegerField(
                        db_column="categoryID", primary_key=True, serialize=False
                    ),
                ),
                (
                    "categoryname",
                    models.CharField(
                        blank=True, db_column="categoryName", max_length=50, null=True
                    ),
                ),
                (
                    "categorydescription",
                    models.CharField(
                        blank=True,
                        db_column="categoryDescription",
                        max_length=100,
                        null=True,
                    ),
                ),
            ],
            options={"db_table": "categories", "managed": False,},
        ),
    ]

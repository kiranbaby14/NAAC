# Generated by Django 4.1 on 2022-08-25 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Ssr_Text_Converter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("college_name", models.CharField(max_length=100, null=True)),
                ("university_name", models.CharField(max_length=100, null=True)),
                ("courses_offered", models.IntegerField(null=True)),
                ("total_no_of_students", models.IntegerField(null=True)),
                ("pdf", models.FileField(blank=True, null=True, upload_to="")),
                ("progress_bar", models.IntegerField(default=0, null=True)),
                ("status", models.CharField(default="None", max_length=100, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ssr_Plot",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("excel", models.FileField(blank=True, null=True, upload_to="")),
                ("status", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ssr_Geo_Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("img", models.ImageField(blank=True, null=True, upload_to="")),
                ("latitude", models.CharField(max_length=100, null=True)),
                ("longitude", models.CharField(max_length=100, null=True)),
                ("lat_convert", models.CharField(max_length=100, null=True)),
                ("long_convert", models.CharField(max_length=100, null=True)),
                ("status", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Iiqa",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, null=True)),
                ("head", models.CharField(max_length=100, null=True)),
                ("designation", models.CharField(max_length=100, null=True)),
                (
                    "own_campus",
                    models.BooleanField(
                        choices=[(True, "Yes"), (False, "No")], default=False
                    ),
                ),
                (
                    "phn_no_clg",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                (
                    "phn_no_principal",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                (
                    "phn_no_principal_alt",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                ("address", models.CharField(max_length=200, null=True)),
                ("city", models.CharField(max_length=100, null=True)),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("---", "---"),
                            ("Andhra Pradesh", "Andhra Pradesh"),
                            ("Arunachal Pradesh", "Arunachal Pradesh"),
                            ("Assam", "Assam"),
                            ("Bihar", "Bihar"),
                            ("Chhattisgarh", "Chhattisgarh"),
                            ("Goa", "Goa"),
                            ("Gujarat", "Gujarat"),
                            ("Haryana", "Haryana"),
                            ("Himachal Pradesh", "Himachal Pradesh"),
                            ("Jharkhand", "Jharkhand"),
                            ("Karnataka", "Karnataka"),
                            ("Kerala", "Kerala"),
                            ("Madhya Pradesh", "Madhya Pradesh"),
                            ("Maharashtra", "Maharashtra"),
                            ("Manipur", "Manipur"),
                            ("Meghalaya", "Meghalaya"),
                            ("Mizoram", "Mizoram"),
                            ("Nagaland", "Nagaland"),
                            ("Odisha", "Odisha"),
                            ("Punjab", "Punjab"),
                            ("Rajasthan", "Rajasthan"),
                            ("Sikkim", "Sikkim"),
                            ("Tamil Nadu", "Tamil Nadu"),
                            ("Telangana", "Telangana"),
                            ("Tripura", "Tripura"),
                            ("Uttar Pradesh", "Uttar Pradesh"),
                            ("Uttarakhand", "Uttarakhand"),
                            ("Gairsain", "Gairsain"),
                            ("West Bengal", "West Bengal"),
                        ],
                        default=1,
                        max_length=100,
                        null=True,
                    ),
                ),
                ("pincode", models.CharField(max_length=100, null=True)),
                ("autonomous_status_date", models.CharField(max_length=100, null=True)),
                ("institution_type", models.CharField(max_length=100, null=True)),
                ("location", models.CharField(max_length=100, null=True)),
                ("financial_status", models.CharField(max_length=100, null=True)),
                ("status", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

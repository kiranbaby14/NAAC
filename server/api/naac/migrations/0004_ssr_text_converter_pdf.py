# Generated by Django 4.1 on 2022-08-22 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("naac", "0003_remove_ssr_text_converter_pdf"),
    ]

    operations = [
        migrations.AddField(
            model_name="ssr_text_converter",
            name="pdf",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
    ]

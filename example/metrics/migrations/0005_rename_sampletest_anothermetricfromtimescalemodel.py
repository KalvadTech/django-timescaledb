# Generated by Django 3.2 on 2021-04-20 19:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("metrics", "0004_metric_device"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="SampleTest",
            new_name="AnotherMetricFromTimeScaleModel",
        ),
    ]

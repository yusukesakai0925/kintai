# Generated by Django 3.2 on 2023-02-23 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0006_auto_20230223_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendances',
            name='leave_emotions',
            field=models.CharField(max_length=64, null=True),
        ),
    ]

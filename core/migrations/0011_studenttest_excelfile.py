# Generated by Django 4.2.7 on 2024-01-22 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_studenttest_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='studenttest',
            name='excelFile',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
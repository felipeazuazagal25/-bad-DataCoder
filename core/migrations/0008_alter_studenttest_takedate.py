# Generated by Django 4.2.7 on 2024-01-22 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_studenttest_status_alter_studenttest_takedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studenttest',
            name='takedate',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
# Generated by Django 4.2.7 on 2024-01-23 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_rename_takedate_studenttest_takedateend_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='rubric',
            field=models.FileField(default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='studenttest',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'No rendido'), (2, 'En curso'), (3, 'Por revisar'), (4, 'Revisado')], default=1),
        ),
    ]

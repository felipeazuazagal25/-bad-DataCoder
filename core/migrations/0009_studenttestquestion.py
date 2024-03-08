# Generated by Django 4.2.7 on 2024-01-22 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_studenttest_takedate'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentTestQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scoreStudent', models.FloatField(null=True)),
                ('questionTest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.question', verbose_name='Question Test')),
                ('studentTest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.studenttest', verbose_name='Student Test')),
            ],
        ),
    ]

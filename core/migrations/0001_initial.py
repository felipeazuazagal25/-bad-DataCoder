# Generated by Django 4.2.7 on 2024-01-22 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0002_remove_user_is_admin_user_is_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortname', models.CharField(max_length=8, unique=True)),
                ('fullname', models.CharField(max_length=64, unique=True)),
                ('semester', models.CharField(max_length=16)),
            ],
            options={
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('userModel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.course', verbose_name='Course')),
            ],
            options={
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='TestQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testName', models.SlugField(max_length=32)),
                ('questionNumber', models.CharField(max_length=3)),
                ('questionVersion', models.CharField(max_length=3)),
                ('questionText', models.TextField()),
                ('questionScore', models.DecimalField(decimal_places=1, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='StudentTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=1, max_digits=3)),
                ('courseName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.course', verbose_name='Course')),
                ('quesitonScore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.testquestions', verbose_name='Questions')),
                ('studentName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student', verbose_name='Student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.SlugField(max_length=32)),
                ('code', models.SlugField(max_length=16)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student', verbose_name='Student')),
            ],
        ),
    ]

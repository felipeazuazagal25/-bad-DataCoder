# Generated by Django 4.2.7 on 2024-01-14 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_course_student_testquestions_fileupload_uploaded_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.RemoveField(
            model_name='studenttest',
            name='courseName',
        ),
        migrations.RemoveField(
            model_name='studenttest',
            name='quesitonScore',
        ),
        migrations.RemoveField(
            model_name='studenttest',
            name='studentName',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='StudentTest',
        ),
        migrations.DeleteModel(
            name='TestQuestions',
        ),
    ]

# Generated by Django 5.1.3 on 2024-11-29 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('only_course', '0002_alter_course_end_at_alter_course_start_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='name',
            new_name='title',
        ),
    ]

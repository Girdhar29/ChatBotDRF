# Generated by Django 5.1.4 on 2024-12-18 11:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0005_alter_student_age"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="user",
        ),
    ]

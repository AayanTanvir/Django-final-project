# Generated by Django 5.1.1 on 2024-09-26 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_choice_submission_question_choice_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice_text',
            new_name='content',
        ),
    ]

# Generated by Django 4.1 on 2022-11-05 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_choice_correct_choice_mark_alter_choice_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='mark',
        ),
    ]

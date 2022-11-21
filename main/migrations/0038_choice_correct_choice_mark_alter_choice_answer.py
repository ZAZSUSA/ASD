# Generated by Django 4.1 on 2022-08-26 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_alter_choice_answer_alter_choice_ip_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='correct',
            field=models.CharField(max_length=200, null=True, verbose_name='Правильный'),
        ),
        migrations.AddField(
            model_name='choice',
            name='mark',
            field=models.CharField(max_length=200, null=True, verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Вариант'),
        ),
    ]
# Generated by Django 4.1 on 2022-11-09 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_remove_choice_mark'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='answer5',
            field=models.CharField(max_length=200, null=True, verbose_name='Вариант5'),
        ),
    ]

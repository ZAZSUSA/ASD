# Generated by Django 4.0.6 on 2022-08-03 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_test_answer1_alter_test_answer2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='Название статьи'),
        ),
    ]

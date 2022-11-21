# Generated by Django 4.0.6 on 2022-08-03 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_test_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='Никнейм'),
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(null=True, verbose_name='Текст комментария'),
        ),
    ]
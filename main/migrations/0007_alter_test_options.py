# Generated by Django 4.0.6 on 2022-08-01 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_article_options_alter_test_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='test',
            options={'verbose_name': 'Тест', 'verbose_name_plural': 'Тесты'},
        ),
    ]

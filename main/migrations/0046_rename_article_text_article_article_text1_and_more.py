# Generated by Django 4.1 on 2022-11-12 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0045_rename_article_img1_test_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='article_text',
            new_name='article_text1',
        ),
        migrations.AddField(
            model_name='article',
            name='article_text10',
            field=models.TextField(null=True, verbose_name='Текст статьи'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_text2',
            field=models.TextField(null=True, verbose_name='Текст статьи'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_text3',
            field=models.TextField(null=True, verbose_name='Текст статьи'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_text4',
            field=models.TextField(null=True, verbose_name='Текст статьи'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_text5',
            field=models.TextField(null=True, verbose_name='Текст статьи'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_text6',
            field=models.TextField(null=True, verbose_name='Текст статьи'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_text7',
            field=models.TextField(null=True, verbose_name='Текст статьи'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_text8',
            field=models.TextField(null=True, verbose_name='Текст статьи'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_text9',
            field=models.TextField(null=True, verbose_name='Текст статьи'),
        ),
    ]

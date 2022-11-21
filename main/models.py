from django.db import models
from django.db.models import ImageField
from django.urls import reverse

class Article(models.Model):
    article_title = models.CharField('Название урока', max_length=200)
    article_img1 = models.ImageField(upload_to="image/", null=True, blank=True)
    article_img2 = models.ImageField(upload_to="image/", null=True, blank=True)
    article_text1 = models.TextField('Текст статьи')
    article_text2 = models.TextField('Текст статьи', null=True)
    article_text3 = models.TextField('Текст статьи', null=True)
    article_text4 = models.TextField('Текст статьи', null=True)
    article_text5 = models.TextField('Текст статьи', null=True)
    article_text6 = models.TextField('Текст статьи', null=True)
    article_text7 = models.TextField('Текст статьи', null=True)
    article_text8 = models.TextField('Текст статьи', null=True)
    article_text9 = models.TextField('Текст статьи', null=True)
    article_text10 = models.TextField('Текст статьи', null=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.article_title

    def get_absolute_url(self):
        return reverse("main:detail", kwargs={"slug": self.slug})

    def get_test_url(self):
        return reverse("main:test_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'



class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('Никнейм', max_length=200)
    text = models.TextField('Текст комментария')


class Test(models.Model):
    question = models.CharField('Вопрос', max_length=200)
    img = models.ImageField(upload_to="image/", null=True, blank=True)
    answer1 = models.CharField('Вариант1', max_length=200)
    answer2 = models.CharField('Вариант2', max_length=200)
    answer3 = models.CharField('Вариант3', max_length=200)
    answer4 = models.CharField('Вариант4', max_length=200)
    answer5 = models.CharField('Вариант5', max_length=200, null=True)
    correct = models.CharField('Правильный вариант ответа', max_length=200)
    slug = models.SlugField(null=False, unique=False)

    def get_test_url(self):
        return reverse("main:test_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Choice(models.Model):
    ip = models.CharField('IP', max_length=200, null=True)
    question = models.CharField('Вопрос', max_length=200, null=True)
    answer = models.CharField('Вариант', max_length=200, null= True)
    correct = models.CharField('Правильный', max_length=200, null= True)
    slug = models.SlugField(null=True, unique=False)
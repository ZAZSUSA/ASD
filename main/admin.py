from django.contrib import admin
from .models import Article, Test, Comment, Choice

admin.site.register(Test)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Choice)
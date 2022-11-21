from django.shortcuts import render, get_object_or_404
from .models import Article, Test, Choice
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def section(request):
    article = Article.objects.order_by('-id')
    return render(request, 'main/section.html', {'title':'Теория', 'article': article})

def tests(request):
    article = Article.objects.order_by('-id')
    return render(request, 'main/tests.html', {'title':'Теория', 'article': article})



def leave_comment(request, slug):
    a = Article.objects.get(slug=slug)
    a.comment_set.create(author_name=request.user, text=request.POST['text'])

    return HttpResponseRedirect(reverse('main:detail', args=(slug,)))



def test_detail(request, slug):
    tests = Test.objects.filter( slug=slug)
    context = {'tests':tests, 'slug':slug}
    return render(request, 'main/test_detail.html', context)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def article_detail(request, slug):
    model = Article.objects.get( slug = slug)
    comments = model.comment_set.order_by('-id')
    context = {'object': model, 'comments':comments, 'slug':slug}
    return render(request, 'main/article_detail.html', context)


def leave_test(request, slug):
    global c
    global m
    c = 0
    '''user = request.user
                choices = Choice.objects.filter( slug=slug) 
                for choice in choices:
                    if str(choice.ip) == str(user):
                        choice.delete()
                    '''
    user = get_client_ip(request)
    choices = Choice.objects.filter( slug=slug) 
    for choice in choices:
        if str(choice.ip) == str(user):
            choice.delete()
    tests = Test.objects.filter( slug=slug) 
    m = len(tests)
    ip = user
    for test in tests:

        answer = request.POST[test.question]
        
        if answer == test.correct:
            a = Choice(ip=ip, question=test.question, answer=answer, correct=test.correct, slug=slug)
            a.save()
            c = c + 1
        else:
            a = Choice(ip=ip, question=test.question, answer=answer, correct=test.correct, slug=slug)
            a.save()
    return HttpResponseRedirect(reverse('main:result', args=(slug,)))

def result(request, slug):
    d = c
    f = m
    ip = get_client_ip(request)
    user = request.user
    user = str(user)
    tests = Test.objects.filter( slug=slug)
    choices = Choice.objects.filter(slug=slug)
    context = {'tests':tests,'slug':slug, 'ip':ip, 'choices':choices, 'c':d, 'm':f, 'user':user}
    return render(request, 'main/result.html', context)

def registration(request):
    return render(request, 'main/registration.html')

def registration_result(request):
    username = request.POST['username']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    userpost = request.POST['userpost']
    try:
        user = User.objects.get(username=username)
        error = 'Имя пользователя занято'
        return render(request, 'main/registration.html', {'error':error})
    except User.DoesNotExist:
        if password1 != password2:
            error = 'Пароли должны быть одинаковыми'
            return render(request, 'main/registration.html', {'error':error})
        else:
            user = User.objects.create_user(username, userpost, password1)
            user.save()
            user = authenticate(request, username=username, password=password1)
            login(request, user)
            return HttpResponseRedirect(reverse('main:home', args=()))

def qwe(request):
    return render(request, 'main/authenticate.html')

def authenticate_result(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('main:home'))
    else:
        error = 'Неверный пароль или имя пользователя'
        return render(request, 'main/authenticate.html', {'error':error})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:home'))
    

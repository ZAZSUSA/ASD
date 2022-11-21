from django.urls import path
from .views import index, about, section, tests,  test_detail, leave_comment, article_detail, leave_test, result, registration, registration_result, qwe, logout_user, authenticate_result
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('', section, name='home'),
    path('about', about, name='about'),
    path('section', section, name='section'),
    path('tests', tests, name='tests'),
    path('section/<slug:slug>', article_detail, name='detail'),
    path('section/<slug:slug>/leave_comment', leave_comment, name='leave_comment'),
    path('tests/<slug:slug>', test_detail, name='test_detail'),
    path('tests/<slug:slug>/leave_test', leave_test, name='leave_test'),
    path('tests/<slug:slug>/result', result, name='result'),
    path('registration', registration, name='registration'),
    path('registration_result', registration_result, name='registration_result'),
    path('authenticate', qwe, name='authenticate'),
    path('authenticate/result', authenticate_result, name='authenticate_result'),
    path('logout_user', logout_user, name='logout_user'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



from .models import Choice
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class AuthUser(forms.ModelForm):
	class Meta:
		model = Choice
		fields = ('username', 'password')

from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Answer, Policy

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username','email']

class Feedback(ModelForm):
	class Meta:
		model = Answer
		fields=['answer','age','gender','region']

class CreatePolicy(ModelForm):
	class Meta:
		model = Policy
		fields = ['name','summary']
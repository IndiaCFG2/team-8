from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Feedback






class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class FeedbackForm(forms.ModelForm):
	
	class Meta:
		model = Feedback
		fields = ['policy','answer','gender','age','location','rating']
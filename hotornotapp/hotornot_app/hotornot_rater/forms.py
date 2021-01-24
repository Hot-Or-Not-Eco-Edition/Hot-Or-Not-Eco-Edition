from django import forms
from .models import *

class SignupForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username", "password", "first_name", "last_name"]

class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username", "password"]
from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
	username = forms.CharField(label="Username",
				max_length=30,
				required=True)
	password = forms.CharField(label="Password",
				max_length=30,
				required=True,
				widget=forms.PasswordInput)


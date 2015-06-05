from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
	#username = forms.CharField(label="Username",
	#			max_length=30,
	#			required=True)
	email = forms.EmailField(label="E-mail",
				required=True)
        first_name = forms.CharField(label="First name",
                                     max_length=30,
                                     required=True)
        last_name = forms.CharField(label="Last name",
                                    max_length=30,
                                    required=True)
	password = forms.CharField(label="Password",
				max_length=30,
				required=True,
				widget=forms.PasswordInput)
	password2 = forms.CharField(label="Confirm password",
				max_length=30,
				required=True,
				widget=forms.PasswordInput,
				)
	#def usernameFree(self, username):
	#	try:
	#		User.objects.get(username=username)
	#	except User.DoesNotExist:
	#		return True
	#	return False
	
	def emailNotRegistered(self, email):
		try:
			#User.objects.get(email=email)
			User.objects.get(username=email)
		except User.DoesNotExist:
			return True
		return False

	def clean(self):
		#username = self.cleaned_data.get("username")
		email = self.cleaned_data.get("email")
		first_name = self.cleaned_data.get('first_name')
		last_name = self.cleaned_data.get('last_name')
		password1 = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("password2")
	
		# check if username already exists
		#if not self.usernameFree(username):
		#	raise forms.ValidationError("Username already registered.")
		
		# check if e-mail is already registered
		
		if not self.emailNotRegistered(email):
                    self.add_error('email', "E-mail already registered")
                    #raise forms.ValidationError("E-mail already registered.")
	
		# check password strength
		# TODO

		if password1 and password1 != password2:
                    self.add_error('password', "Passwords don't match")
                    #raise forms.ValidationError("Passwords don't match")
		
		return self.cleaned_data
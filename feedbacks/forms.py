from django import forms
from django.contrib.auth.models import User

class WriteFeedbackForm(forms.Form):
        feedback = forms.CharField(label='Feedback',
                                     max_length=255,
                                     required=True,
                                     widget=forms.Textarea)
        
        anonymous = forms.BooleanField(label='Anonymous',
                                    initial=True,
                                    required=False)

	def clean(self):
		feedback  = self.cleaned_data.get("feedback")
		anonymous = self.cleaned_data.get("anonymous")
		return self.cleaned_data
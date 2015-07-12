from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['email', 'full_name']
	
	def clean_email(self):
		email =  self.cleaned_data.get('email')
		if not "com" in email:
			raise forms.ValidationError("Please use a valid .com email adress")
		return email	

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		return full_name
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import SignUpForm, ContactForm

# Create your views here.
def home(request):
	title = "Hi"
	form = SignUpForm(request.POST or None)
	context = {
		"template_title": title,
		"form":form,

	}
	if form.is_valid():
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		instance.full_name = full_name
		instance.save()
	context = {
		"template_title": "Thank You",
		

	}
	
	return render(request, "home.html", context)


def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")

		subject = "Site Contact Form"
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email,	"info@fifart.net"]
		contact_message = "%s:%s via %s" % (form_full_name, form_message, form_email)
		send_mail(subject, contact_message, from_email, to_email, fail_silently=False)


	context = {
		"template_title": "Contact Us",
		"form":form,
	}


	return render(request, "forms.html", context)	
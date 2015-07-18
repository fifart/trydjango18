from django.shortcuts import render
from .forms import SignUpForm

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
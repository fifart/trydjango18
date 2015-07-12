from django.shortcuts import render

# Create your views here.
def home(request):
	title = "Hi"
	if request.user.is_authenticated():
		title = "Welcome %s" % (request.user)
	context = {
		"template_title": title,

	}
	return render(request, "home.html", context)
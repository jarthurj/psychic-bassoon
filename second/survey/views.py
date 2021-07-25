from django.shortcuts import render, HttpResponse

def index(request):
	return render(request, "index.html")
def results(request):
	context = {
		"name":request.POST['name'],
		"email":request.POST['email'],
		"language":request.POST['langs'],
		"other_lanuage":request.POST['langs2'],
		"comment":request.POST['comment'],
	}
	return render(request, "results.html", context)

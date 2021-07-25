from django.shortcuts import render, HttpResponse, redirect

def index(request):
	return render(request, "index.html")


def process_results(request):
	request.session["name"]=request.POST['name']
	request.session["email"]=request.POST['email']
	request.session["language"]=request.POST['langs']
	request.session["other_lanuage"]=request.POST['langs2']
	request.session["comment"]=request.POST['comment']
	return redirect("/results")
def results(request):
	return render(request, "results.html")



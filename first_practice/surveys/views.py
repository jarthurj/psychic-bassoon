from django.shortcuts import render, HttpResponse

def index(request):
	return HttpResponse("Placeholder to display all the surverys created")
def new(request):
	return HttpResponse("Placeholder for users to add a new survey")
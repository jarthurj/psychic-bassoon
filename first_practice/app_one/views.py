from django.shortcuts import render, HttpResponse, redirect

def index(request):
	return HttpResponse("Place hodler to later display a list of all blogs")

def new(request):
	return HttpResponse("placeholder to display a new form ot create a new blog")

def create(request):
	return redirect("/")

def show(request, blog_number):
	return HttpResponse("display blog number"+ str(blog_number))

def edit(request, blog_number):
	return HttpResponse("placeholder to edit blog" + str(blog_number))

def destroy(request, blog_number):
	return redirect("/")
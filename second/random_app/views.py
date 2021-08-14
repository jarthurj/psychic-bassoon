from django.utils.crypto import get_random_string
from django.shortcuts import render, HttpResponse, redirect
def index(request):
	if request.method == 'POST':
		request.session['counter'] += 1
	elif request.method == 'GET':
		request.session['counter'] = 1
	context = {
		'counter':request.session['counter'],
		'random': get_random_string(length=14)
	}
	return render(request, "index.html", context)
def reset(request):
	request.session.flush()
	return redirect('/random_app')
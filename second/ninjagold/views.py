from django.shortcuts import render, redirect
import random
def index(request):
	if 'current_gold' not in request.session:
		request.session['current_gold'] = 0
	context = {
		'current_gold':request.session['current_gold'],
		'activites': 'butt'
	}
	return render(request, "ninja_gold_index.html", context)

def process_gold(request, typer):
	win_lose = random.randint(0,1)
	ranges = {
		'farm':[10,20],
		'cave':[5,10],
		'house':[2,5],
		'casino':[0,50],
	}
	if typer == 'casino':
		if win_lose == 1:
			request.session['current_gold'] += random.randint(*ranges[typer])
		else:
			request.session['current_gold'] -= random.randint(*ranges[typer])
	else:
		request.session['current_gold'] += random.randint(*ranges[typer])
	return redirect('/ninja_gold')
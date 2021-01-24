from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages



# Create your views here.
def index(request):
	return render(request, 'index.html', {})

def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST or None)

		if form.is_valid():
			form.save()
			return redirect('index')

	else:
		return render(request, 'signup.html', {})

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST or None)
		if form.is_valid():
			return redirect('index')

	else:
		return render(request, 'login.html', {})


def leaderboard(request):
	db = ld.objects.all().order_by('-score')
	context = {'data': db}
	return render(request, 'leaderboard.html', context)

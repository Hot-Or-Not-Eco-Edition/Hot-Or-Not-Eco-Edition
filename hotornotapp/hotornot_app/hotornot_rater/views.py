from django.shortcuts import render
from .models import *
from .forms import *


# Create your views here.
def index(request):
	return render(request, 'index.html', {})

def signup(request):

	if request.method == 'POST':
		form = SignupForm(request.POST or None)

		if form.is_valid():
			form.save()
			return render(request, 'index.html', {})

	else:
		return render(request, 'signup.html', {})

def login(request):
	return render(request, 'login.html', {})

def leaderboard(request):
	leader = [['Toronto', '500'], ['Montreal', '400'], ['Vancouver', '300'], ['Calgary', '200'], ['Edmonton', '600'], ['Ottawa', '250'], ['Winnipeg', '350'], ['Quebec City', '175'], ['Kitchener', '256'], ['Halifax', '268'], ['Victoria', '412']]
	leader = sorted(leader, key=lambda x: x[1], reverse=True)
	context = {'data': leader}
	return render(request, 'leaderboard.html', context)
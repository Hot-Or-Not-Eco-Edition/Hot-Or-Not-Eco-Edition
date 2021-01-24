from django.shortcuts import render
from .models import Leaderboard as ld #renamed due to possible name conflict

# Create your views here.
def index(request):
	return render(request, 'index.html', {})

def signup(request):
	return render(request, 'signup.html', {})

def login(request):
	return render(request, 'login.html', {})

def leaderboard(request):
	db = ld.objects.all().order_by('-score')
	context = {'data': db}
	return render(request, 'leaderboard.html', context)
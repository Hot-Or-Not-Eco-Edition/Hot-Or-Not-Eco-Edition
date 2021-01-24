from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
	return render(request, 'index.html', {})

def signup(request):
	return render(request, 'signup.html', {})

def login(request):
	return render(request, 'login.html', {})

def leaderboard(request):
	return render(request, 'leaderboard.html', {})
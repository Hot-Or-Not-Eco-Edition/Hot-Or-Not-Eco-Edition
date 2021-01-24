from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.conf import settings
import os
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
	db = Leaderboard.objects.all().order_by('-score')
	context = {'data': db}
	return render(request, 'leaderboard.html', context)


# Create your views here. 
def photos(request): 
	db = Images.objects.all()
	content = {"photos": db}
	return render(request, 'photos.html', content)

def image_upload(request): 
    if request.method == 'POST': 
        form = ImagesForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = ImagesForm() 
    return render(request, 'upload.html', {'form' : form}) 
  
  
def success(request): 
    return render(request, 'success.html', {})

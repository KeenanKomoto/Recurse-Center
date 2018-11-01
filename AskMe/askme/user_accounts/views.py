from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'user_accounts/index.html')

def settings(request):
    return render(request, 'user_accounts/settings.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'user_accounts/signup.html', {'form': form})

def confirmation(request):
    return render(request, 'user_accounts/confirmation.html')

def homepage(request):
    return render(request, 'user_accounts/homepage.html')

from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.

def signup(request):
    if request.method == 'POST':
        if request.POST['pw1'] == request.POST['pw2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username is in use'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['pw1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html',{'error': 'Error: You have insufficient mastery over your password.'})
    else:
        return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['pw'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error':'Fool, have you forgotten your password?'})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('logout')
    return redirect('home')

from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(
                request,
                username=username,
                password=password
            )
            login(request, user)
            return redirect('/account')
    else:
        form = RegistrationForm()

    args = {'form': form}
    return render(request, 'accounts/register.html', args)

def profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)

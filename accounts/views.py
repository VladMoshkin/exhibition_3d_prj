from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def logout_user(request):
    redirect_url = '/'
    if 'next' in request.GET:
        redirect_url = request.GET['next']
    logout(request)
    print(request.get_full_path())
    return HttpResponseRedirect(redirect_url)

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
            return redirect('/accounts')
    else:
        form = RegistrationForm()

    args = {'form': form}
    return render(request, 'accounts/register.html', args)

@login_required
def profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)

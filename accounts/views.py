from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

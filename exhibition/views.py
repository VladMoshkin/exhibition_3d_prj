from django.shortcuts import render, get_object_or_404
from exhibition.models import *
from django.utils import timezone
from .models import Exhibition

def exhibition_list(request):
    exhibitions = Exhibition.objects.all()[:6]
    #exhibition = get_object_or_404(Exhibition, slug=exhibition_slug)
    #images = Image.objects.filter(exhibition=exhibition,approved=True)
    context = {"exhibitions":exhibitions}
    return render(request, 'pages/exhibition/exhibition_list.html', context)

def exhibition_detail(request, pk):
    exhibition = get_object_or_404(Exhibition, pk=pk)
    return render(request, 'pages/exhibition/exhibition_detail.html', {'exhibition': exhibition})

def about(request):
    return render(request, 'pages/exhibition/about_us.html', {})

def profile(request):
    return render(request, 'pages/exhibition/profile.html', {})

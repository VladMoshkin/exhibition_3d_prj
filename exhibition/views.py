from django.shortcuts import render, get_object_or_404
from exhibition.models import *

def exhibition_list(request):
    exhibitions = Exhibition.objects.all()[:6]
    #exhibition = get_object_or_404(Exhibition, slug=exhibition_slug)
    #images = Image.objects.filter(exhibition=exhibition,approved=True)
    context = {"exhibitions":exhibitions}
    return render(request, 'pages/exhibition/exhibition_list.html', context)

def about(request):
    return render(request, 'pages/exhibition/about_us.html', {})

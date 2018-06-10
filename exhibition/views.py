from django.shortcuts import render, get_object_or_404
from exhibition.models import *
from django.utils import timezone
from .models import Exhibition
from PIL import Image
import json

def exhibition_list(request):
    exhibitions = Exhibition.objects.filter(open_date__lte=timezone.now()).order_by('-open_date')
    #exhibition = get_object_or_404(Exhibition, slug=exhibition_slug)
    #images = Image.objects.filter(exhibition=exhibition,approved=True)
    context = {"exhibitions":exhibitions}
    return render(request, 'pages/exhibition/exhibition_list.html', context)

def exhibition_list_grid(request):
    exhibitions = Exhibition.objects.filter(open_date__lte=timezone.now()).order_by('-open_date')
    context = {"exhibitions":exhibitions}
    return render(request, 'pages/exhibition/exhibition_list_grid.html', context)

def images_to_json(images):
    result_images = {}
    for image in images:
        url = image.image.url
        width = image.image.width
        height = image.image.height
        ratio = width/height
        result_images[image.id]={ 'url': url,
                                  'height': height,
                                  'width': width,
                                  'ratio': ratio,
                                  'title': image.title,
                                  'author': image.author.username }
    result_images = json.dumps(result_images)
    return result_images

def exhibition_detail(request, pk):
    exhibition = get_object_or_404(Exhibition, pk=pk)
    images = exhibition.image_set.all()
    json_images = images_to_json(images)
    print(images)
    context = {'exhibition': exhibition, 'images': json_images}
    return render(request, 'pages/exhibition/exhibition_detail.html', context)

def exhibition_addimage(request):
    exhibitions = Exhibition.objects.filter(open_date__gte=timezone.now()).order_by('-open_date')
    context = {"exhibitions":exhibitions}
    return render(request, 'pages/exhibition/exhibitions_addimage.html', context)

def about(request):
    return render(request, 'pages/exhibition/about_us.html', {})

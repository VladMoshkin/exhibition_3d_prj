from django.shortcuts import render, get_object_or_404
from exhibition.models import *
from django.utils import timezone
from .models import Image

def addimage(request):
    return render(request, 'pages/image/addimage.html', {})

from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from image.forms import AddImage
from exhibition.models import Exhibition
from image.models import Image

def addimage(request, pk):
    form = AddImage()
    exhibition = get_object_or_404(Exhibition, pk=pk)
    user = request.user
    context = {'form': form}
    if Image.objects.filter(author=user, exhibition=exhibition).exists():
        old_image = Image.objects.filter(author=user, exhibition=exhibition).first()
        context['old_image'] = old_image
    if request.method == 'POST':
        print(request.POST)
        image, created = Image.objects.get_or_create(
                                    exhibition=exhibition,
                                    author=user,
                                    defaults={
                                    'title': request.POST['title'],
                                    'image': request.POST['image']
                                    })
    return render(request, 'pages/image/addimage.html', context )

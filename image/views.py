from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from image.forms import AddImage
from exhibition.models import Exhibition
from image.models import Image
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def addimage(request, pk):
    form = AddImage()
    exhibition = get_object_or_404(Exhibition, pk=pk)
    user = request.user
    context = {'form': form}
    if Image.objects.filter(author=user, exhibition=exhibition).exists():
        old_image = Image.objects.filter(author=user, exhibition=exhibition).first()
        context['old_image'] = old_image
    if request.method == 'POST':
        print(request.POST, request.FILES)
        image, created = Image.objects.get_or_create(
                                    exhibition=exhibition,
                                    author=user,
                                    defaults={
                                    'title': request.POST['title'],
                                    'image': request.POST and request.FILES['image']
                                    })
        return redirect( reverse('addimage', kwargs={'pk':pk}))
    return render(request, 'pages/image/addimage.html', context )

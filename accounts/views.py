from django.shortcuts import render

# Create your views here.
def profile(request):
    return render(request, 'pages/exhibition/exhibition_list.html',)

from django.shortcuts import render

def exhibition_list(request):
    return render(request, 'exhibition/exhibition_list.html', {})


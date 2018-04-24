from django.shortcuts import render

def exhibition_list(request):
    return render(request, 'pages/exhibition/exhibition_list.html', {})


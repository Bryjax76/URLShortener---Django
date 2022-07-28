from django.shortcuts import render

def index(request):
    if True:
        return render(request, 'index.html')
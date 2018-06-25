from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'message': 'This is the home page...'})

def others(request):
    return HttpResponse('Hello, this is the others page...')

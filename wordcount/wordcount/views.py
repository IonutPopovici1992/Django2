from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello, this is the home page...')

def others(request):
    return HttpResponse('Hello, this is the others page...')

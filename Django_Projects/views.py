from django.http import HttpResponse

def index(request):
    return HttpResponse('hello woorld')

def home(request):
    return HttpResponse('<h5>Welcome to the Home Page</h5>')
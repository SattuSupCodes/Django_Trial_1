from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
   return render(request, 'index.html')
def hello(request):
    return HttpResponse("hello")



# i feel sooooooooooooooooooooooooooooooooooooooo fucked but hey, that's life of an engineer
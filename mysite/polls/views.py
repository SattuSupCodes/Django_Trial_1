from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
   context = { 'name' : 'Sattu',
              'age': 20,
               'nation':'India'}
   return render(request, 'index.html', context)

   
def hello(request):
   pass

def app(request):
   context = {
      'name' : 'name',
      
   }
   return render(request, 'tryapp.html', context)


# i feel sooooooooooooooooooooooooooooooooooooooo fucked but hey, that's life of an engineer
from django.shortcuts import render

#from django.http import HttpResponse
# Create your views here.
from catalog.models import Catalog


def home(request):
    #return HttpResponse('This is home page')
    context = {
        'title':'Home title',
        'catalog' : Catalog.objects.all(),
    }
    return render(request, 'default_app/home.html', context)



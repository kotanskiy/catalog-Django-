from django.shortcuts import render
from catalog.models import Catalog
# Create your views here.

def home(request):
    context = {
        'title':'Home title',
        'catalog' : Catalog.objects.all(),
    }
    return render(request, 'default_app/home.html', context)



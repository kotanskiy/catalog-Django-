from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from catalog.models import Catalog
# Create your views here.

def catalog_home(request):
    context = {
        'page_header': 'Catalog page',
        'catalog': Catalog.objects.all(),
    }
    return render(request, 'catalog/catalog.html', context)

def catalog_details(request, catalog_id):
    catalog_item = get_object_or_404(Catalog, pk=catalog_id)
    context = {
        'page_header': catalog_item.title,
        'catalog':catalog_item,
    }
    return render(request, 'catalog/catalog_detail.html', context)

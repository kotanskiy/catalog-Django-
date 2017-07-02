from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from catalog.models import Catalog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def catalog_home(request):

    catalog_list = Catalog.objects.all()
    paginator = Paginator(catalog_list, 2)
    page = request.GET.get('page')
    try:
        catalog = paginator.page(page)
    except PageNotAnInteger:
        catalog = paginator.page(1)
    except EmptyPage:
        catalog = paginator.page(paginator.num_pages)

    if page == '1':
        return redirect('catalog:home', permanent=True)

    context = {
       'page_header': 'Catalog page',
       'catalog': catalog,
    }
    return render(request, 'catalog/catalog.html', context)

def catalog_details(request, catalog_id):
    catalog_item = get_object_or_404(Catalog, pk=catalog_id)
    context = {
        'page_header': catalog_item.title,
        'catalog':catalog_item,
    }
    return render(request, 'catalog/catalog_detail.html', context)



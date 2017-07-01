from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

def home(request):
    #return HttpResponse('This is home page')
    context = {
        'title' : 'Home title'
    }
    return render(request, 'default_app/home.html', context)



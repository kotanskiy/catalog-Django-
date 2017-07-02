from django.conf.urls import url
from . import views


app_name = 'catalog'
urlpatterns = [
    url(r'^$', views.catalog_home, name='home'),
    url(r'^(?P<catalog_id>[\d+]*)$', views.catalog_details, name='details'),
]
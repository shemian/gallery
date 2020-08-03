from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .import views


urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^search/', views.search_results, name='search'),
    url(r'^location/(?P<location>\w+)/', views.image_location, name='location'),
    url(r'^category/(?P<category>\w+)/', views.image_category, name='category'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  

from django.urls import include
from django.urls import path as url
from . import views


app_name = 'home'

urlpatterns = [
    url(r'', views.home, name='home'),
    url(r'about', views.about, name='about'),
    url(r'service', views.service, name='service'),
    url(r'portfolio', views.portfolio, name='portfolio'),
    url(r'download', views.download, name='download'),
    url(r'contact/', views.contact, name='contact'),
    url(r'contactF/', views.contactF, name='contactF'),
]
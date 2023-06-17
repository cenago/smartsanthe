from . import views
from django.urls import include
from django.urls import path as url
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'home'

urlpatterns = [
    url(r'', views.home, name='home'),
    url(r'about', views.about, name='about'),
    url(r'service', views.service, name='service'),
    url(r'portfolio', views.portfolio, name='portfolio'),
    url(r'download', views.download, name='download'),
    # url(r'report', views.report, name='report'),
    url(r'contact/', views.contact, name='contact'),
    url(r'contactF/', views.contactF, name='contactF'),
    url('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
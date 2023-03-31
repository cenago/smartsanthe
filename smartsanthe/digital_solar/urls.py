from .views import digital_volt
from django.urls import path

urlpatterns = [
    path('v1/', digital_volt.as_view()),

]
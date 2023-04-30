from .views import digital_volt, report
from django.urls import path

app_name = 'digital_solar'

urlpatterns = [
    path('v1/', digital_volt.as_view()),
    path(r'report', report, name='report'),
]



from django.contrib import admin
from .models import Customer, Device, Panels, Voltages

# Register your models here.
admin.site.register(Customer)
admin.site.register(Panels)
admin.site.register(Device)
admin.site.register(Voltages)

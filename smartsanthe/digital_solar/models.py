from django.db import models

# Create your models here.


class Panels(models.Model):

    panels_id = models.CharField(max_length=200)
    wat = models.IntegerField()
    max_volt = models.IntegerField()
    panel_dim = models.CharField(max_length=200)

    class Meta:
        # otherwise we get "Tutorial Seriess in admin"
        verbose_name_plural = "Panels"

    def __str__(self):
        return self.panels_id


class Device(models.Model):

    device_id = models.CharField(max_length=200)
    panels_id = models.CharField(max_length=200)
    logitude = models.FloatField()
    latitude = models.FloatField()

    class Meta:
        verbose_name_plural = "Device"

    def __str__(self):
        return self.device_id


class Customer(models.Model):
    bill_no = models.CharField(max_length=200)
    bill_date = models.DateField()
    ammount = models.IntegerField()
    owner_name = models.CharField(max_length=200)
    tt_divice = models.IntegerField()
    tt_panels = models.IntegerField()
    service_status = models.IntegerField(default='')
    address = models.CharField(max_length=200, default='')
    mobile = models.CharField(max_length=10, default='')
    device_id = models.ForeignKey('Device', related_name='Device', on_delete=models.CASCADE)
    panels_id = models.ForeignKey('Panels', related_name='Panels', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Customer"

    def __str__(self):
        return self.bill_no


class Voltages(models.Model):

    volt = models.IntegerField()
    time_instance = models.DateTimeField()
    bill_no = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Voltages"

    def __str__(self):
        return str(self.volt)


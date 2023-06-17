from rest_framework import serializers
from .models import Voltages


class VoltageSerializer(serializers.ModelSerializer):

    volt = serializers.IntegerField(required=True)
    temperature = serializers.FloatField(required=True)
    insertdate = serializers.DateTimeField(required=True)
    bill_no = serializers.CharField(max_length=200, required=True)

    class Meta:
        model = Voltages
        fields = ('__all__')
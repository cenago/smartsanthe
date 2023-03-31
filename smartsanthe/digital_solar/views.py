from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Voltages
from .serializers import VoltageSerializer


class digital_volt(APIView):

    def get(self, request, *args, **kwargs):
        result = Voltages.objects.all()
        serializers = VoltageSerializer(result, many=True)
        return Response({'status': 'success', "Voltages": serializers.data}, status=200)

    def post(self, request):
        serializer = VoltageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
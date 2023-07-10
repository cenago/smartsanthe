<<<<<<< HEAD
# import numpy as np
import io, base64
import matplotlib.pyplot as plt
=======
>>>>>>> d30691f5c0e19ed94123b6666cb79c2a9e9e1b93

import io, base64
from . import models
from .models import Voltages
import matplotlib.pyplot as plt
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import VoltageSerializer
from rest_framework.permissions import IsAuthenticated


def report(request):

    data = models.Voltages.objects.all()
    print("report")
    s = []
    t = []
    for i in data:
        s.append(i.volt)
        t.append(i.insertdate)
    # max_year = models.Voltages.objects.latest('time_instance')


    fig, ax = plt.subplots()
    ax.plot(t[-5:], s[-5:])

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
           title='About as simple as it gets, folks')
    ax.grid()

    flike = io.BytesIO()
    fig.savefig(flike)
    b64 = base64.b64encode(flike.getvalue()).decode()

    return render(request, 'home/plotxxreport.html',
                  { "chart": b64}, status=200)


class digital_volt(APIView):
    permission_classes = (IsAuthenticated,)

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


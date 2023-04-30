import numpy as np
import io, base64
import matplotlib.pyplot as plt

from . import models
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Voltages
from .serializers import VoltageSerializer

def report(request):

    data = models.Voltages.objects.all()
    print("report")
    s = []
    t = []
    for i in data:
        # print(i.volt)
        # print(i.time_instance, type(i.time_instance))
        # print(i.bill_no)
        s.append(i.volt)
        t.append(i.time_instance)
    max_year = models.Voltages.objects.latest('time_instance')
    # models.Voltages.objects.
    # print(max_year.time_instance, "max_year", max_year._id)
    expos = models.Voltages.objects.filter(id="1").values()
    print(expos[0]['volt'],
    expos[0]['time_instance'],
    expos[0]['bill_no'], "Max date record")
    # Data for plotting
    # t = np.arange(0.0, 2.0, 0.01)
    # s = 1 + np.sin(2 * np.pi * t)
    #
    # t = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9
    #      ]
    #
    # s = [1, 3, 1, 2, 4, 3, 2, 4, 6, 4]

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
           title='About as simple as it gets, folks')
    ax.grid()

    flike = io.BytesIO()
    fig.savefig(flike)
    b64 = base64.b64encode(flike.getvalue()).decode()


    return render(request, 'home/plotxxreport.html',
                  { "chart": b64}, status=200)


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


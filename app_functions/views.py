from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from django.views.generic import CreateView, TemplateView
from .models import FunctionFourierSeriesModel, FunctionsTaylorSeriesModel
from .serializers import FunctionsFourierSerializer, FunctionsTaylorSerializer
import matplotlib.pyplot as plt
from django.http import HttpRequest
import io
import urllib, base64
from math import sin, cos, pi, factorial

# Create your views here.

class FourierSeriesCreateView(CreateView):
    model = FunctionFourierSeriesModel
    fields = 'a0', 'a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'b3', 'b4', 'l', 'name', 'description'
    template_name = 'app_functions/tmplt.html'

class FourierSeriesPlotView(TemplateView):
    def get(self, request: HttpRequest, pk: int):
        obj = get_object_or_404(FunctionFourierSeriesModel, pk=pk)
        def series(x):
            result = 0
            result = result + obj.a0/2
            result = result + obj.a1*cos(x*pi/obj.l)
            result = result + obj.a2*cos(x*pi*2/obj.l)
            result = result + obj.a3*cos(x*pi*3/obj.l)
            result = result + obj.a4*cos(x*pi*4/obj.l)
            result = result + obj.b1*sin(x*pi/obj.l)
            result = result + obj.b2*sin(x*pi*2/obj.l)
            result = result + obj.b3*sin(x*pi*3/obj.l)
            result = result + obj.b4*sin(x*pi*4/obj.l)
            return result

        fig, ax = plt.subplots()
        ax.plot([(float(x*0.001)) for x in range(int(obj.l*1000))], [series(float(x*0.001)) for x in range(int(obj.l*1000))])
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri =  urllib.parse.quote(string)
        context = {
            'source': uri
        }
        return render(request, template_name='app_functions/show_fig.html', context=context)

class FourierSeriesAPIView(APIView):
    def get(self, request, format=None):
        obj = FunctionFourierSeriesModel.objects.all()
        serializer = FunctionsFourierSerializer(obj, many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FunctionsFourierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FourierSeriesAPIViewSet(ViewSet):
    queryset = FunctionFourierSeriesModel.objects.all()
    serializer_class = FunctionsFourierSerializer


class TaylorSeriesAPIView(APIView):
    def get(self, request, format=None):
        obj = FunctionsTaylorSeriesModel.objects.all()
        serializer = FunctionsTaylorSerializer(obj, many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FunctionsTaylorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TaylorSeriesPlotView(TemplateView):
    def get(self, request: HttpRequest, pk: int):
        obj = get_object_or_404(FunctionsTaylorSeriesModel, pk=pk)
        def series(x):
            result = 0
            result = result + obj.c0
            result = result + obj.c1*(x-obj.x0)
            result = result + obj.c2*(((x-obj.x0)**2)/factorial(2))
            result = result + obj.c3*(((x-obj.x0)**3)/factorial(3))
            result = result + obj.c4*(((x-obj.x0)**4)/factorial(4))
            result = result + obj.c5*(((x-obj.x0)**5)/factorial(5))
            result = result + obj.c6*(((x-obj.x0)**6)/factorial(6))
            result = result + obj.c7*(((x-obj.x0)**7)/factorial(7))
            result = result + obj.c8*(((x-obj.x0)**8)/factorial(8))
            return result

        fig, ax = plt.subplots()
        ax.plot([(float(x*0.001)) for x in range(int(3140))], [series(float(x*0.001)) for x in range(int(3140))])
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri =  urllib.parse.quote(string)
        context = {
            'source': uri
        }
        return render(request, template_name='app_functions/show_fig.html', context=context)
    
class TaylorSeriesCreateView(CreateView):
    model = FunctionsTaylorSeriesModel
    fields = 'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'x0', 'name', 'description'
    template_name = 'app_functions/tmplt.html'

class FourierSeriesDerivativePlotView(TemplateView):
    def get(self, request: HttpRequest, pk: int):
        obj = get_object_or_404(FunctionFourierSeriesModel, pk=pk)
        def series(x):
            result = 0
            result = result - obj.a1*sin(x*pi/obj.l)*(pi/obj.l)
            result = result - obj.a2*sin(x*pi*2/obj.l)*(pi*2/obj.l)
            result = result - obj.a3*sin(x*pi*3/obj.l)*(pi*3/obj.l)
            result = result - obj.a4*sin(x*pi*4/obj.l)*(pi*4/obj.l)
            result = result + obj.b1*cos(x*pi/obj.l)*(pi/obj.l)
            result = result + obj.b2*cos(x*pi*2/obj.l)*(pi*2/obj.l)
            result = result + obj.b3*cos(x*pi*3/obj.l)*(pi*3/obj.l)
            result = result + obj.b4*cos(x*pi*4/obj.l)*(pi*4/obj.l)
            return result

        fig, ax = plt.subplots()
        ax.plot([(float(x*0.001)) for x in range(int(obj.l*1000))], [series(float(x*0.001)) for x in range(int(obj.l*1000))])
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri =  urllib.parse.quote(string)
        context = {
            'source': uri
        }
        return render(request, template_name='app_functions/show_fig.html', context=context)

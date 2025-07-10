from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from django.views.generic import CreateView, TemplateView
from .models import FunctionFourierSeriesModel
import matplotlib.pyplot as plt
from django.http import HttpRequest
import io
import urllib, base64
from math import sin, cos, pi

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




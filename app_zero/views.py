from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from django.views.generic import CreateView, TemplateView
from .models import ZeroModel, ZeroImageModel, ZeroStringModel
from .forms import ZeroSubmitForm
from .figures import sin_figure
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import io
import urllib, base64
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ZeroSerializer
# Create your views here.


class ZeroSubmitView(TemplateView):
    form_class = ZeroSubmitForm
    template_name = 'app_zero/input_zero'

class ZeroShowView(TemplateView):
    template_name = 'app_zero/show_sin'
    def get_context_data(self, **kwargs):
        a = self.request.GET.get('a')
        b = self.request.GET.get('b')
        dx = self.request.GET.get('dx')
        w = self.request.GET.get('w')
        context = super().get_context_data(**kwargs)
        fig = sin_figure(a=int(a),b=int(b),dx=float(dx),w=float(w))
        #fig = context['test']
        #fig.show()
        #graph = ZeroModel(fig=sin_figure(a=int(a),b=int(b),dx=float(dx),w=float(w)))
        #graph = ZeroModel.objects.create()
        #graph.fig=context['test']
        #context['test'].show()
        #graph.save()
        #img = ZeroImageModel.objects.create()
        #img.img.filename = 'app_zero/static/graph.png'
        #img.save()
        buf = io.BytesIO()
        #graph = ZeroModel.objects.get(id=64)
        #graph.fig.source 
        #graph.save()
        fig.savefig(buf,format='png')
        img = ZeroImageModel.objects.create()

        filepath='uploads/test_img_{id}.png'
        fig.savefig(filepath.format(id=img.id))
        img.img=filepath.format(id=img.id)
        img.save()
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri =  urllib.parse.quote(string)
        img_str = ZeroStringModel.objects.create(source=uri)
        context['test'] = uri
        #graph = ZeroModel.objects.create()
        #graph.fig.source = uri
        #img = ZeroImageModel.objects.create()
        #img.img.filename = 'data:image/png;base64,{uri}'
        return context
    
class ZeroFromBaseShowView(TemplateView):
    def get(self, request: HttpRequest, pk: int):
        obj = get_object_or_404(ZeroModel, pk=pk)
        context = {
            'obj': obj.fig
        }
        return render(request, template_name='app_zero/show_fig.html', context=context)

class ZeroCreateView(CreateView):
    model = ZeroModel
    fields = 'fig',

def home(request):
    plt.plot(range(10))
    fig = plt.gcf()
    #convert graph into dtring buffer and then we convert 64 bit code into image
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri =  urllib.parse.quote(string)
    return render(request,'app_zero/show_sin_alt.html',{'data':uri})

class ZeroImageView(TemplateView):
    def get(self, request: HttpRequest, pk: int):
        obj = get_object_or_404(ZeroImageModel, pk=pk)
        context = {
            'obj': obj.img
        }
        return render(request, template_name='app_zero/show_image.html', context=context)
    
class ZeroListStringView(TemplateView):
    template_name = 'app_zero/show_all_images.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_list'] = ZeroStringModel.objects.all()
        return context
    
class ZeroAPIView(APIView):
    def get(self, request):
        queryset = ZeroStringModel.objects.all()
        zero_serializer = ZeroSerializer(
            instance = queryset,
            many = True
        )
        return Response(zero_serializer.data)
    
class ZeroAPIViewOne(APIView):
    def get(self, request, pk):
        queryset = ZeroStringModel.objects.get(pk=pk)
        zero_serializer = ZeroSerializer(
            instance = queryset
        )
        return Response(zero_serializer.data)
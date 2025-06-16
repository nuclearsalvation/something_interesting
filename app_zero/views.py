from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from django.views.generic import CreateView, TemplateView
from .models import ZeroModel, ZeroImageModel, ZeroStringModel, ZeroNameNumModel,  ZeroCSVModel
from .forms import ZeroSubmitForm
from .figures import sin_figure, response_figure
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import io, csv
import urllib, base64
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import renderers
from .serializers import ZeroSerializer, ZeroResponseSerializer, ZeroNameNumSerializer
from rest_framework import status
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

class ZeroResponseView(TemplateView):
    template_name = 'app_zero/show_sin'
    def get_context_data(self, **kwargs):
        fin = self.request.GET.get('fin')
        a = self.request.GET.get('a')
        b = self.request.GET.get('b')
        c = self.request.GET.get('c')
        dx = self.request.GET.get('dx')
        context = super().get_context_data(**kwargs)
        fig = response_figure(fin=int(fin),a=float(a),b=float(b),c=float(c),dx=float(dx))
        buf = io.BytesIO()
        fig.savefig(buf,format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri =  urllib.parse.quote(string)
        context['test'] = uri             
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
    
class ZeroNameNumCreateView(TemplateView):
    template_name = 'app_zero/show_name_num.html'
    def get_context_data(self, **kwargs):
        name = self.request.GET.get('name')
        num = self.request.GET.get('num')
        context = super().get_context_data(**kwargs)
        context['name'] = name
        context['num'] = float(num)*1.85             
        #context['name'] = [name, num]
        return context

class ZeroLoadFromCSVView(TemplateView):
    template_name='app_zero/show_name_num_set.html'
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loading_list = []
        with open('uploads/table.csv','r', encoding='utf-8') as loading_file:
            csv_reader = csv.reader(loading_file)
            next(csv_reader, None)
            for row in csv_reader:
                loading_list.append(row)
        context['name_num_list'] = loading_list
        return context
    
class ZeroCSVCreateView(CreateView):
    model = ZeroCSVModel
    template_name = 'app_zero/tmplt.html'

class ZeroResponseSubmitView(TemplateView):
    template_name ='app_zero/input_response.html'

class ZeroResponseAPIView(APIView):
    def get(self, request):
            class LocalClass:
                def __init__(self, fin, a, b, c, dx, created=None):
                    self.fin = fin
                    self.a = a
                    self.b = b 
                    self.c = c
                    self.dx = dx

            fin = self.request.GET.get('fin')
            a = self.request.GET.get('a')
            b = self.request.GET.get('b')
            c = self.request.GET.get('c')
            dx = self.request.GET.get('dx')
            srlz = LocalClass(fin,a,b,c,dx)
            serializer = ZeroResponseSerializer(srlz)
            fig = response_figure(fin=int(fin),a=float(a),b=float(b),c=float(c),dx=float(dx))
            img = ZeroImageModel.objects.create()

            filepath='uploads/test_img_{id}.png'
            fig.savefig(filepath.format(id=img.id))
            img.img=filepath.format(id=img.id)
            img.save()
            return Response(serializer.data)
    
class ZeroNameNumAPIView(APIView):
    def get(self, request, format = None):
        obj = ZeroNameNumModel.objects.all()
        serializer = ZeroNameNumSerializer(obj, many = True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ZeroNameNumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ZeroLoadFromCSVViewToDB(TemplateView):
    template_name='app_zero/show_name_num_set.html'
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loading_list = []
        with open('uploads/table.csv','r', encoding='utf-8') as loading_file:
            csv_reader = csv.reader(loading_file)
            next(csv_reader, None)
            for row in csv_reader:
                loading_list.append(row)
        context['name_num_list'] = loading_list
        for name_num in loading_list:
            ZeroNameNumModel.objects.create(name = name_num[0], num=name_num[1])
        return context
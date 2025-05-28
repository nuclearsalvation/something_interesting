from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .models import ZeroModel
from .forms import ZeroSubmitForm
from .figures import sin_figure
import matplotlib
import matplotlib.pyplot as plt
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
        context['test'] = sin_figure(int(a),int(b),float(dx),float(w))
        return context
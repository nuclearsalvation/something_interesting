from django.urls import path
from .views import *

app_name = 'app_functions'

urlpatterns = [
    path('create_fourier', FourierSeriesCreateView.as_view(template_name='app_functions/tmplt.html'), name='create_fourier'),
    path('show_fourier/<pk>', FourierSeriesPlotView.as_view(template_name='app_functions/show_fig.html'), name='plot_fourier')
]
from django.urls import path
from .views import *

app_name = 'app_functions'

urlpatterns = [
    path('create_fourier', FourierSeriesCreateView.as_view(template_name='app_functions/tmplt.html'), name='create_fourier'),
    path('show_fourier/<pk>', FourierSeriesPlotView.as_view(template_name='app_functions/show_fig.html'), name='plot_fourier'),
    path('show_fourier/<pk>/derivative', FourierSeriesDerivativePlotView.as_view(template_name='app_functions/show_fig.html'), name='plot_fourier_derivative'),
    path('api_fourier', FourierSeriesAPIView.as_view()),
    path('api_taylor', TaylorSeriesAPIView.as_view()),
    path('show_taylor/<pk>', TaylorSeriesPlotView.as_view(template_name='app_functions/show_fig.html'), name='plot_taylor'),
    path('create_taylor', TaylorSeriesCreateView.as_view(template_name='app_functions/tmplt.html'), name='create_taylor'),
    path('show_taylor/<pk>/derivative', TaylorSeriesDerivativePlotView.as_view(template_name='app_functions/show_fig.html'), name='plot_taylor_derivative'),
]
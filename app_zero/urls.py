from django.urls import path
from .views import ZeroSubmitView, ZeroShowView, ZeroFromBaseShowView, ZeroCreateView,  ZeroImageView, ZeroListStringView

app_name='app_zero'

urlpatterns=[
    path('submit', ZeroSubmitView.as_view(template_name='app_zero/input_zero.html'), name='submit'),
    path('sin', ZeroShowView.as_view(template_name='app_zero/show_sin.html'), name='sin'),
    path('show/<pk>', ZeroFromBaseShowView.as_view(template_name='app_zero/show_fig.html'), name='show'),
    path('create', ZeroCreateView.as_view(template_name='app_zero/tmplt.html'), name='create'),
    path('show_image/<pk>', ZeroImageView.as_view(template_name='app_zero/show_image.html'), name='show_image'),
    path('show_all', ZeroListStringView.as_view(template_name='app_zero/show_all_images.html'), name='show_all')


]
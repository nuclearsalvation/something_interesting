from django.urls import path
from .views import ZeroSubmitView, ZeroShowView

app_name='app_zero'

urlpatterns=[
    path('submit', ZeroSubmitView.as_view(template_name='app_zero/input_zero.html'), name='submit'),
    path('sin', ZeroShowView.as_view(template_name='app_zero/show_sin.html'), name='sin')

]
from django.urls import path
from .views import ZeroSubmitView, ZeroShowView, ZeroFromBaseShowView, ZeroCreateView,  ZeroImageView, ZeroListStringView, ZeroAPIView, ZeroAPIViewOne, ZeroResponseView, ZeroNameNumCreateView, ZeroLoadFromCSVView, ZeroResponseSubmitView, ZeroResponseAPIView, ZeroNameNumAPIView, ZeroLoadFromCSVViewToDB, ZeroResponseAPIViewTwo, ZeroResponseAPIViewMany, ZeroNameNumAPIViewOne, ZeroSubmitFileView, ZeroDampingAPIViewMany, ZeroJSONCreateView

app_name='app_zero'

urlpatterns=[
    path('submit', ZeroSubmitView.as_view(template_name='app_zero/input_zero.html'), name='submit'),
    path('sin', ZeroShowView.as_view(template_name='app_zero/show_sin.html'), name='sin'),
    path('show/<pk>', ZeroFromBaseShowView.as_view(template_name='app_zero/show_fig.html'), name='show'),
    path('create', ZeroCreateView.as_view(template_name='app_zero/tmplt.html'), name='create'),
    path('show_image/<pk>', ZeroImageView.as_view(template_name='app_zero/show_image.html'), name='show_image'),
    path('show_all', ZeroListStringView.as_view(template_name='app_zero/show_all_images.html'), name='show_all'),
    path('serialized', ZeroAPIView.as_view()),
    path('serialized/<pk>',ZeroAPIViewOne.as_view()),
    path('response', ZeroResponseView.as_view(template_name='app_zero/show_sin.html'), name='response'),
    path('name_num', ZeroNameNumCreateView.as_view(template_name='app_zero/show_name_num.html'), name='name_num'),
    path('name_num_all', ZeroLoadFromCSVView.as_view(template_name='app_zero/show_name_num_set.html'), name='name_num_list'),
    path('submit_response', ZeroResponseSubmitView.as_view(template_name='app_zero/input_response.html'), name='submit_response'),
    path('serialized_response', ZeroResponseAPIView.as_view()),
    path('create_num_name', ZeroNameNumAPIView.as_view()),
    path('name_num_all_db', ZeroLoadFromCSVViewToDB.as_view(template_name='app_zero/show_name_num_set.html'), name='name_num_list_db'),
    path('serialized_response_two', ZeroResponseAPIViewTwo.as_view()),
    path('serialized_response_many', ZeroResponseAPIViewMany.as_view()),
    path('name_num_one/<pk>', ZeroNameNumAPIViewOne.as_view()),
    path('submit_file', ZeroSubmitFileView.as_view(template_name='app_zero/submit_file.html'), name='submit_file'),
    path('serialized_damping_many', ZeroDampingAPIViewMany.as_view()),
    path('create_json', ZeroJSONCreateView.as_view(template_name='app_zero/tmplt.html'), name='create_json')

]
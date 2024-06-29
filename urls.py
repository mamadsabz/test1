from django.urls import path
from product_module.views import *

urlpatterns = [
    path('' , product_list , name='product_list'),
    path('detail/', product_detail, name='product_detail'),
]


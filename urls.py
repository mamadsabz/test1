from django.urls import path
from home_module.views import *


urlpatterns = [
    path('', home, name='home'),
]
from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', user_list, name='user_list'),
]
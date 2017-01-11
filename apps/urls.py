from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^mycaps/$', MyCaps.as_view(), name='mycaps'),
]
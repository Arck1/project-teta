from django.urls import path, include, re_path
from show import views

urlpatterns = [
    re_path(r'(?P<id>\d+)/(?P<hash>\w+)/$', views.showcase, name='showcase'),
]

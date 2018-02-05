from django.urls import path
from landing import views

urlpatterns = [
    path(r'', views.index, name='index')
]

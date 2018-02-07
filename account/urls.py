from django.urls import path, include, re_path
from account import views

urlpatterns = [
    path('presentations/', views.account_info, name='account'),
    re_path(r'presentations/(?P<id>\d+)/$', views.presentation_info, name='presentation'),
    path('presentations/add/', views.add_presentation, name='add'),
    path('', views.account_info, name='account'),
]

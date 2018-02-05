from django.urls import path, include, re_path
from authsys import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('registrate/', views.registrate, name='registrate')
]

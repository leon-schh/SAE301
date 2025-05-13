from django.urls import path
from . import views


urlpatterns = [

    path('', views.login, name='login'), 
    path('login', views.login, name='login'),  
    path('Led', views.Led, name='Led'),
    path('main', views.main, name='main'),
    
]
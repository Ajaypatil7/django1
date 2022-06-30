
from django.urls import path
from app1 import views 
name='app1'
urlpatterns = [
     path('appview1/', views.appview1, name='appview1'),
    
]

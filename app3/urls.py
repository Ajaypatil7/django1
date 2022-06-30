
from django.urls import path
from app3 import views 
urlpatterns=[
    path('appview3/', views.appview3, name='appview3'),
]
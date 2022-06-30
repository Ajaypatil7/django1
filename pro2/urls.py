"""pro2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from pro2 import views
import app1
import app2
import app3
urlpatterns = [
    path('admin/', admin.site.urls),
    path('proview/', views.proview, name='proview'), 
    # path('appview1/', v1.appview1, name='appview1'),
    # path('appview2/', v2.appview2, name='appview2'),
    # path('appview3/', v3.appview3, name='appview3'),
    path('app1/', include("app1.urls")),
    path('app2/', include("app2.urls")),
    path('app3/', include("app3.urls")),

]

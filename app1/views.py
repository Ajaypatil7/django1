from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def appview1(request):
    return HttpResponse('<h1> Inside the App1 views file<h1>')
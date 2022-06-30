from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def appview2(request):
    return HttpResponse('<h1> Inside the App2 views file<h1>')
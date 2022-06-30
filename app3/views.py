from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def appview3(request):
    return HttpResponse('<h1> Inside the App3 views file<h1>')


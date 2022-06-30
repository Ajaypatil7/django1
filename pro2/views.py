from django.http import HttpResponse
from django.shortcuts import render

def proview(request):
    return render(request, 'sample1.html')



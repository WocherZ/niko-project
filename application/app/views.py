from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
# Create your views here.
def register(request):
    if request.method == 'POST':
        pass
    else:
        return HttpResponseNotAllowed()

def authorization(request):
    if request.method == 'POST':
        pass
    else:
        return HttpResponseNotAllowed()
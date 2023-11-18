from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def kane(request):
    return HttpResponse('<h1> coolest captain ever')
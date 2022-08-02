from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home (request):
    return HttpResponse("Hello I am Working :) ")
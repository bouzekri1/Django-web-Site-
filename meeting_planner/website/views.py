from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to the Metting Planner ! ")


def date(request):
    return HttpResponse("This page was served at " +str(datetime.now()))

def text(request):
    return HttpResponse("Hello my name is Abdessamad Im trying to learn Django")
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("HOME PAGE")


def about(request):
    return HttpResponse("ABOUT PAGE")


def contact(request):
    return HttpResponse("CONTACT PAGE")

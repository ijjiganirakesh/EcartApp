from django.shortcuts import HttpResponse,render

def home(request):
    return HttpResponse("hello world")

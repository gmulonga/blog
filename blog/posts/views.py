from django.shortcuts import render
from django.http import HttpResponse

def post_home(request):
    return HttpResponse("<h1>hello World!</h1>")

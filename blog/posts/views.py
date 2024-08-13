from django.shortcuts import render
from django.http import HttpResponse

def post_detail(request):
    return HttpResponse("<h1>Home</h1>")

def post_list(request):
    return HttpResponse("<h1>Post list</h1>")

def post_add(request):
    return HttpResponse("<h1>Add post</h1>")

def post_update(request):
    return HttpResponse("<h1>Post Update</h1>")

def post_delete(request):
    return HttpResponse("<h1>Post delete</h1>")


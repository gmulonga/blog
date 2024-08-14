from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title": "list"
    }
    return render(request, "index.html", context)
def post_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "post_detail.html", context)

def post_add(request):
    return HttpResponse("<h1>Add post</h1>")

def post_update(request):
    return HttpResponse("<h1>Post Update</h1>")

def post_delete(request):
    return HttpResponse("<h1>Post delete</h1>")


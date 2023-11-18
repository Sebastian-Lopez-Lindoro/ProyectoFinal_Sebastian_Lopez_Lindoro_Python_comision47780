from django.shortcuts import render

# Create your views here.


def inicio(request):
    return render(request, "Blog/index.html")


def pages(request):
    return render(request, "Blog/pages.html")


def about(request):
    return render(request, "Blog/about.html")

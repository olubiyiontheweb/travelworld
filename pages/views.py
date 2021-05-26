from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "pages/index.html")


def base(request):
    return render(request, "layout/base.html")

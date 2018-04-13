from django.shortcuts import render

def render_homepage(request):
    return render(request, 'home/home.html')

def render_aboutpage(request):
    return render(request, 'home/about.html')
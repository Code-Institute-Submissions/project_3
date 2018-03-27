from django.shortcuts import render

def render_homepage(request):
    return render(request, 'home/home.html')
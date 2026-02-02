from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.




def landing_page_view(request):
    return render(request, "project/home.html")

def about_view(request):
    return render(request, "project/about.html")
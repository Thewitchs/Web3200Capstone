from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def landing_page_view(request):
    return HttpResponse(f"<h1>Book Site</h1><p>Welcome! This site is underconstruction!</p>
                        

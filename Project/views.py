from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Book


# Create your views here.




def landing_page_view(request):
    return render(request, "project/home.html")

def about_view(request):
    return render(request, "project/about.html")

def index(request):
    books = Book.objects.all().order_by('dds')
    return render(request, 'home.html', {
        'books': books
    })

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)

    return render(request, 'project/detail.html', {
        'book': book
    })
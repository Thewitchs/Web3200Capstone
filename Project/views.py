from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import Book
from .form import ReviewForm
from django.views.generic import ListView, DetailView
from .models import Feedback



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


def feedback(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/submission')
    else:
        form = ReviewForm()

    return render(request, 'project/app_review.html', {
        'form': form
    })

class FeedbackListView(ListView):
    model = Feedback
    template_name = "project/feedback_list.html"
    context_object_name = "feedbacks"


class FeedbackDetailView(DetailView):
    model = Feedback
    template_name = "project/feedback_detail.html"
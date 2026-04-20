from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Book
from .forms import ReviewForm, BookForm
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from .models import Feedback



# Create your views here.


def landing_page_view(request):
    return render(request, "project/home.html")
def book_list(request):
    return render(request, "project/book_list.html")

def about_view(request):
    return render(request, "project/about.html")

def index(request):
    books = Book.objects.all().order_by('dds')
    return render(request, 'project/home.html', {
        'books': books
    })

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)

    return render(request, 'project/detail.html', {
        'book': book.title,
        'pages': book.pages
    })
def book_form(request):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/book_list')

    else:
        form = BookForm()

    return render(request, 'project/book_form.html', {
        'form': form
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

class SubmissionView(TemplateView):
        template_name = "project/submission.html"
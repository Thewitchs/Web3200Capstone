from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page_view, name="home"),
    path("about", views.about_view, name="about"),
    path("book_list", views.book_list, name="book-list"),
    path('books/<slug:slug>/', views.book_detail, name='book-detail'),
    path("reviews", views.FeedbackListView.as_view(), name="feedback-list"),
    path("reviews/<int:pk>/", views.FeedbackDetailView.as_view(), name="feedback_detail"),
    path("app_review/", views.feedback, name='app-review'),
    path("book_form/", views.book_form, name= "book-form"),
    path("submission", views.SubmissionView.as_view(), name= 'submission'),

    ]

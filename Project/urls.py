from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page_view, name="home"),
    path("about/", views.about_view, name="about"),
    path('books/<slug:slug>/', views.book_detail, name='book-detail'),
    path("reviews/", views.FeedbackListView.as_view(), name="feedback_list"),
    path("reviews/<int:pk>/", views.FeedbackDetailView.as_view(), name="feedback_detail"),



    ]

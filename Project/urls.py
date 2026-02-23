from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page_view, name="home"),
    path("about/", views.about_view, name="about"),
     path('books/<slug:slug>/', views.book_detail, name='book-detail'),



    ]

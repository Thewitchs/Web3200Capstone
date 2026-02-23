from django.contrib import admin
from .models import Book, BookMetadata, Publisher, Genre

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_filter = ('author', 'pages')
    search_fields = ('title', 'author', 'pages')

admin.site.register(Book, BookAdmin)
admin.site.register(BookMetadata)
admin.site.register(Publisher)
admin.site.register(Genre)

from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.


#many to one
class Publisher(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
#many to many
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    




class Book(models.Model):
    title = models.CharField(max_length=10000)
    author = models.CharField(max_length=3000)
    pages = models.IntegerField()
    dds = models.FloatField(null=True)
    slug = models.SlugField(default='', null=False, db_index=True )

    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    genre = models.ManyToManyField(Genre)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('book-detail', args=[self.slug])
    

    def __str__(self):
        return f"{self.title}"
    
    #one to one
class BookMetadata(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, null=True)
    isbn = models.CharField(max_length=13)
    publication_date= models.DateField()
    summary = models.TextField()

    def __str__(self):
        return f"Metadata for {self.book.title}"

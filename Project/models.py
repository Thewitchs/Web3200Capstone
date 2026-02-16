from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=10000)
    author = models.CharField(max_length=3000)
    pages = models.IntegerField()
    dds = models.FloatField(null=True)
    slug = models.SlugField(default='', null=False, db_index=True )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('book-detail', args=[self.slug])
    

    def __str__(self):
        return f"{self.title}"
    

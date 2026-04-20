from django import forms
from .models import Feedback, Book

class ReviewForm (forms.ModelForm):
    image = forms.ImageField()
    class Meta:
        model = Feedback
        fields = '__all__'
        labels = {
            'username': 'Your Name',
            'email': 'Your Email',
            'message': 'Your Feedback', 
            'image': 'Add an Image'
        }

class BookForm (forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


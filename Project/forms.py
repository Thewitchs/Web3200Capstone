from django import forms
from .models import Feedback

class ReviewForm (forms.Form):
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
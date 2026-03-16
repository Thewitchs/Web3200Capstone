from django import forms
from .models import Feedback

class ReviewForm (forms.ModelForm):
    class Meta:
        model = Feedback
        fields = 'all'
        labels = {
            'username': 'Your Name',
            'email': 'Your Email',
            'message': 'Your Feedback', 
        }
from django import forms
from .models import Book

class BookUploadForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'category', 'scholar', 'pdf_file']



class BookReviewForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['status', 'rejection_reason']
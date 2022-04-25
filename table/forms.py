from django import forms
from .models import Table

class Book_table(forms.ModelForm):
    class Meta:
        models = Table
        fields = '__all__'
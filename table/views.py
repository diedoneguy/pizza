from multiprocessing import context
from django.shortcuts import render
from django.urls import is_valid_path

from table.forms import Book_table
from .models import Table
# Create your views here.
def table_book(request):
    table_form = Book_table()
    if table_form == 'POST':
        table_form == Book_table(request.POST)
        if table_form.is_valid():
            table_form.save()
            table_form = Book_table()
    context = {
        'form':table_form,
    }
    return render (request, 'index.html' ,context)
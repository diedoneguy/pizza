from django.urls import path
from .views import table_book

app_name = 'table'
urlpatterns = [
    path('table_book',table_book,name='table_book')
]
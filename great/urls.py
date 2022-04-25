from django.urls import path
from .views import great
app_name = 'great'
urlpatterns = [
    path('sus',great,name ='sus')
]
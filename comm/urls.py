from django.urls import path
from .views import coment
app_name ='comm'
urlpatterns = [
    path('coment',coment,name='coment')
]
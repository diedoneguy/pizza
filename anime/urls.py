from django.urls import path
from .views import menu
# from . import views
app_name = 'anime'
urlpatterns = [
    path('',menu,name ='menu')
]
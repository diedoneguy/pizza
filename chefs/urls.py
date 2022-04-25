from django.urls import path
from .views import chefs
app_name = 'chefs'
urlpatterns = [
    path('chefs',chefs,name='chefs')
]
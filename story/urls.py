from django.urls import path
from .views import story
app_name = 'story'
urlpatterns = [
    path('story',story,name='story')
]
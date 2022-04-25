from multiprocessing import context
from django.shortcuts import render
from .models import Story

# Create your views here.
def story(request):
    star = Story.objects.all()
    context = {
        'star':star
    }
    return render(request,'index.html',context)
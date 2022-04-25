from multiprocessing import context
from django.shortcuts import render
from .models import Great
# Create your views here.
def great(requst):
    prost = Great.objects.all()
    context = {
        'prost':prost
    }
    return render (requst,'index.html',context)
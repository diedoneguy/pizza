from django.shortcuts import render
from .models import Cafe
from chefs.models import Chef
from comm.models import Comments
from great.models import Great
from story.models import Story
# Create your views here.
def menu(request):
    persons = Chef.objects.all()
    foods = Cafe.objects.all()
    rate = Comments.objects.all()
    prost = Great.objects.all()
    sake = Story.objects.all()

    context = {
        'persons':persons,
        'foods':foods,
        'rate':rate,
        'prost':prost,
        'sake':sake
    }
    return render (request,'index.html',context)
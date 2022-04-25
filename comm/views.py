from django.shortcuts import render
from .models import Comments
# Create your views here.
def coment(request):
    rate = Comments.objects.all()
    context = {
        'rate':rate
    }
    return render (request,'index.html',context)
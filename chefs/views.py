from django.shortcuts import render
from .models import Chef
# Create your views here.
def chefs(request):
    persons = Chef.objects.all()
    context = {
        'persons':persons
    }
    return render(request,'index.html',context)
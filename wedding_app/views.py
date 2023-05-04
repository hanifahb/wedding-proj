from django.shortcuts import render

from django.http import HttpResponse

from .forms import EventForm
from .models import Event

# def index(request):
#     return render (request,'wedding/index.html')

# def about(request):
#     return render (request,'wedding/about.html')


# def contact(request):
#     return render (request,'wedding/contact.html')

def base(request):
    return render (request,'wedding2/base.html')

def events(request):
    if request.method =='POST':
        form=EventForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=EventForm()
    return render (request,'wedding2/events.html', {"form":form})


def chida(request):
    return render (request,'wedding2/chida.html')

def edmunds(request):
    return render (request,'wedding2/edmunds.html')

    

# Create your views here.

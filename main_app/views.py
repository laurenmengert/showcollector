from django.shortcuts import render
from .models import Show


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def shows_index(request):
    shows = Show.objects.all()
    return render(request, 'shows/index.html', {'shows': shows})

def shows_detail(request, show_id):
    show = Show.objects.get(id=show_id)
    return render(request, 'shows/detail.html', {'show': show})
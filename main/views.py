from django.shortcuts import render
from .models import Accord
from django.views.generic import DetailView


def index(request):
    song = Accord.objects.all()
    return render(request, "main/index.html", {'song': song, "title": "Accord"})

class NewsDetailView(DetailView):
    model = Accord
    template_name = 'main/song.html'
    context_object_name = 'song'

def adding(request):
    return render(request, "main/adding.html")
from django.shortcuts import render, redirect
from .models import Accord
from .forms import AccordForm
from django.views.generic import DetailView


def index(request):
    song = Accord.objects.all()
    return render(request, "main/index.html", {'song': song, "title": "Accord"})

class NewsDetailView(DetailView):
    model = Accord
    template_name = 'main/song.html'
    context_object_name = 'song'

def adding(request):
    error = ""
    if request.method == 'POST':
        form = AccordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = "Форма заполнена неверно."

    form = AccordForm()
    data = {'form': form, "error": error}
    return render(request, "main/adding.html", data)

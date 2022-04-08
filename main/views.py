from django.shortcuts import get_list_or_404, render, redirect
from .models import Accord, Artist
from .forms import AccordForm, ArtistForm
from django.views.generic import DetailView


def index(request):
    song = Accord.objects.all()
    return render(request, "main/index.html", {'song': song, "title": "Accord"})

class SongDetailView(DetailView):
    model = Accord
    template_name = 'main/song.html'
    context_object_name = 'song'

def adding(request):
    error = ""
    if request.method == 'POST':
        form_artist = ArtistForm(request.POST)
        form_accord = AccordForm(request.POST)
        if form_artist.is_valid() and form_accord.is_valid():
            item_artist, create = Artist.objects.get_or_create(artist_name=form_artist.data["artist_name"])
            item_form_artist = item_artist
            item_form_accord = form_accord.save(commit=False)
            item_form_accord.artist = item_form_artist
            item_form_accord.save()
            return redirect("home")
        else:
            error = "Форма заполнена неверно."
    form_artist = ArtistForm()
    form_accord = AccordForm()
    data = {'form_artist': form_artist, "form_accord": form_accord, "error": error}
    return render(request, "main/adding.html", data)


def all_songs_artist(request, artist):
    item_artist = Artist.objects.get(url_name=artist)
    songs = get_list_or_404(Accord, artist_id=item_artist)
    return render(request, "main/all_songs_artist.html", {'songs': songs, 'item_artist': item_artist, 'title': artist})


def artists(request):
    all_artist = Artist.objects.all()
    return render(request, "main/artists.html", {'all_artist': all_artist, "title": 'Все исполнители'})

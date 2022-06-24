from django.urls import path
from . import views


urlpatterns = [
        path('', views.SongListView.as_view(), name='home'),
        path('<int:pk_artist>/', views.all_songs_artist, name='all_songs_artist'),
        path('<int:pk_artist>/<int:pk_song>/', views.SongDetailView.as_view(), name='song'),
        path('artists/', views.artists, name='artists'),
        path('adding/', views.adding, name='adding'),
]
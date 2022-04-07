from django.urls import path
from . import views


urlpatterns = [
        path('', views.index, name='home'),
        path('<int:pk>', views.SongDetailView.as_view(), name='song'),
        path('<str:artist>', views.all_songs_artist, name='all_songs_artist'),
        path('artists/', views.artists, name='artists'),
        path('adding/', views.adding, name='adding'),
]
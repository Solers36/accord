from django.urls import path
from . import views


urlpatterns = [
        path('', views.home_favourites, name='home_favourites'),
        # path('<int:pk_artist>/', views.all_songs_artist, name='all_songs_artist'),

]
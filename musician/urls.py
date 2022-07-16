from django.urls import path
from . import views


urlpatterns = [
        path('', views.home_musician, name='home_musician'),
        # path('<int:pk_artist>/', views.all_songs_artist, name='all_songs_artist'),
]
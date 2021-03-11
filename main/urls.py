from django.urls import path
from . import views


urlpatterns = [
        path('', views.index, name='home'),
        path('<int:pk>', views.NewsDetailView.as_view(), name='song'),
        path('adding/', views.adding, name='adding'),
]
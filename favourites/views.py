from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home_favourites(request):
    return render(request, "favourites/home_favourites.html")

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home_musician(request):
    return render(request, "musician/home_musician.html")

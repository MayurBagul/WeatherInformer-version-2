from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Data
from .form import CityForm
from django.contrib.auth.decorators import login_required
import random


def home(request):
    return render(request, 'homepage/home.html', {'title': 'Homepage'})


def about(request):
    return render(request, 'homepage/about.html', {'title': 'About'})


@login_required
def weather(request):

    if request.method == 'POST':
        form = CityForm(request.POST)
    else:
        form = CityForm()

    condition = request.POST.get('city_name')

    data = Data.objects.filter(city__exact=condition)

    info = {'data': data, 'title': 'Weather', 'form': form}

    return render(request, 'homepage/weather.html', info)


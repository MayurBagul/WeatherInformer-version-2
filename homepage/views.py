from django.shortcuts import render
from .models import Data
import random

# temp = random.choice(["26'C", "35'C", "30'C", "20'C", "15'C", ])

# humidity = random.choice(['25%', '26%', '29%', '28%'])

# water_lvl = random.choice(['55%', '56%', '54%', '53%'])


def home(request):
    return render(request, 'homepage/home.html', {'title': 'Homepage'})


def about(request):
    return render(request, 'homepage/about.html', {'title': 'About'})


def weather(request):
    output = Data.objects.all()

    data = random.choice(output)

    info = {'data': data, 'title': 'Weather'}

    return render(request, 'homepage/weather.html', info)


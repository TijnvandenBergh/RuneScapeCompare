from django.shortcuts import render
from django.http import HttpResponse
import requests
from polls.models.Player import Player

# Create your views here.

def index(request):
    response = requests.get('https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player=SmurfPortal')
    player = Player(response.content)
    return render(request, 'home.html', {
    })

def home(request):
    response = requests.get('https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player=SmurfPortal')
    player = Player(response)
    return render(request, 'home.html', {
    })
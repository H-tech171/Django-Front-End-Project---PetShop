from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def dogs(request):
    return render(request, 'pet_wise/dog.html')

def cats(request):    
    return render(request, 'pet_wise/cat.html')

def fishes(request):
    return render(request, 'pet_wise/fish.html')

def lizzards(request):
    return render(request, 'pet_wise/lizzard.html')

def hamsters(request):
    return render(request, 'pet_wise/hamster.html')

def birds(request):
    return render(request, 'pet_wise/bird.html')

def tortoises(request):
    return render(request, 'pet_wise/tortoise.html')

def snakes(request):
    return render(request, 'pet_wise/snake.html')

def hedgehogs(request):
    return render(request, 'pet_wise/hedgehog.html')

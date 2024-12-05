from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('dogs/', dogs, name="dogs"),
    path('cats/', cats, name="cats"),
    path('fishes/', fishes, name="fishes"),
    path('lizzards/', lizzards, name="lizzards"),
    path('hamsters/', hamsters, name="hamsters"),
    path('birds/', birds, name="birds"),
    path('tortoises/', tortoises, name="tortoises"),
    path('snakes/', snakes, name="snakes"),
    path('hedgehogs/', hedgehogs, name="hedgehogs"),
]
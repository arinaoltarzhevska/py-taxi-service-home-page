from django.http import HttpRequest
from .models import Driver, Manufacturer, Car
from django.shortcuts import render


def index(request: HttpRequest) -> render:
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    context = {
        "num_drivers" : num_drivers,
        "num_manufacturers" : num_manufacturers,
        "num_cars" : num_cars,
    }
    return render(request, "taxi/index.html", context=context)

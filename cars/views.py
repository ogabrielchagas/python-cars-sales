from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    #cars = Car.objects.all()
    cars = Car.objects.filter(model__icontains='Chevette Tubarão')

    return render(
        request, 
        'cars.html', 
        {'cars': cars}
    )

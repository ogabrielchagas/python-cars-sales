from django.shortcuts import render
from cars.models import Car
from cars.forms import CarForm

def cars_view(request):
    filter = request.GET.get('search')

    if filter:
        cars = Car.objects.filter(model__icontains=filter).order_by('model')
    else:
        cars = Car.objects.all().order_by('model')

    return render(
        request, 
        'cars.html', 
        {'cars': cars}
    )

def new_car_view(request):
    new_car_form = CarForm()
    return render(request, 'new_car.html', { 'new_car_form': new_car_form }) 

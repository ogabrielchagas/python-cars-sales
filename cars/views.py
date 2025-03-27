from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    filter = request.GET.get('search')

    if filter:
        cars = Car.objects.filter(model__icontains=filter)
    else:
        cars = Car.objects.all()

    return render(
        request, 
        'cars.html', 
        {'cars': cars}
    )

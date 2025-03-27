from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    filter = request.GET.get('search')

    cars = Car.objects.filter(model__icontains=filter)

    return render(
        request, 
        'cars.html', 
        {'cars': cars}
    )

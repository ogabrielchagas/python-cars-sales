from django.db.models.signals import post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory

def car_inventory_update():
    cars_count = Car.objects.all().count()  #Total of cars in inventory
    cars_total_value = Car.objects.aggregate(
        total_value = Sum('value')      #{'total_value': 100.00} returns from query set
    )['total_value']                    #acessing total_value field

    CarInventory.objects.create(        #create a new entry into CarIventory table/model
        cars_count = cars_count,        #With the total of cars calculated before
        cars_total_value = cars_total_value #The total value of those cars
    )

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()
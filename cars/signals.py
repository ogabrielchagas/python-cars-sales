from django.db.models.signals import post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    cars_count = Car.objects.all().count()
    cars_total_value = Car.objects.aggregate(
        total_value = Sum('value')
    )

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    cars_count = Car.objects.all().count()
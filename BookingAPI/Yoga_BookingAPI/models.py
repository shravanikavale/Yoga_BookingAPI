from django.db import models
from django.utils import timezone


class FitnessClass(models.Model):
    name = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    instructor = models.CharField(max_length=100)
    available_slots = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.fitness_class.name}"


class Bookings(models.Model):
    fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    created_at = models.DateTimeField(default=timezone.now)
 
    def __str__(self):
        return f"{self.client_name} - {self.fitness_class.name}"


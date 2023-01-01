from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)])
    heart_rate = models.IntegerField(default=75, validators=[MinValueValidator(15), MaxValueValidator(600)])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

#python manage.py sqlmigrate hospital 0001 --> to see the created sql queries
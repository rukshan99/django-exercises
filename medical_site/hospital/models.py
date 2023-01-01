from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

#python manage.py sqlmigrate hospital 0001 --> to see the created sql queries
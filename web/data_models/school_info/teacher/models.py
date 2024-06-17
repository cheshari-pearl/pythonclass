from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_birth = models.DateField()
    country = models.CharField(max_length=20)
    qualifications = models.CharField(max_length=40)
    age = models.PositiveSmallIntegerField()
    phone_number = models.CharField(max_length=20)
    next_of_kin = models.CharField(max_length=20)
    county = models.CharField(max_length=20)

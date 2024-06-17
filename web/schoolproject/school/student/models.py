from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    code = models.PositiveSmallIntegerField()
    date_of_birth = models.DateField()
    country = models.CharField(max_length=20)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField()
    phone_number = models.CharField(max_length=20)
    # pic = models.ImageField()
    next_of_kin = models.CharField(max_length=20)
    county = models.CharField(max_length=20)





    def __str__(self):
        return f"{self.first_name} {self.last_name}"

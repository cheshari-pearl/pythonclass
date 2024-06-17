from django.db import models

class Course(models.Model):
    course_name= models.CharField(max_length=20)
    course_description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    code = models.PositiveSmallIntegerField()
    course_language = models.CharField(max_length=20)
    materials = models.TextField()
    phone_number = models.PositiveBigIntegerField()
    course_fee = models.CharField(max_length=20)
    course_outline = models.TextField()

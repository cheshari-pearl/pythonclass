from django.db import models

class Classs(models.Model):
    class_name = models.CharField(max_length=20)
    capacity = models.PositiveSmallIntegerField()
    attendance = models.PositiveSmallIntegerField()
    class_projects = models.TextField()
    class_activities = models.TextField()
    class_reps = models.TextField()
    assignments = models.TextField()
    class_rules = models.TextField()
    requirements = models.TextField()
    class_members = models.TextField()


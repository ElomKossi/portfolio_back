from django.db import models

# Education
class Education(models.Model):
    title = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    lacation = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)

# Experience

# Project

# Interest
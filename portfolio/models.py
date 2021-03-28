from django.db import models


# Education
class Education(models.Model):
    """ Model efinition for Education """
    title = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    lacation = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    


# Experience
class Experience(models.Model):
    """ Model efinition for Experience """
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    lacation = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    summary = models.CharField(max_length=500)

    def __str__(self):
        return self.title


# Project
class Project(models.Model):
    """ Model efinition for Project """
    title = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    summary = models.CharField(max_length=500)

    def __str__(self):
        return self.title


# Skill
class Skill(models.Model):
    """ Model efinition for Skill """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Technology
class Technology(models.Model):
    """ Model efinition for Technology """
    name = models.CharField(max_length=50)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Interest
class Interest(models.Model):
    """ Model efinition for Interest """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
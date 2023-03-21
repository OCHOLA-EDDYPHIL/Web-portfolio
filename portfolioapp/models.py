from django.db import models
from django.utils import timezone


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    service = models.CharField(max_length=50)
    opinion = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)


class Application(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now, editable=False)


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    service = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateField(default=timezone.now)


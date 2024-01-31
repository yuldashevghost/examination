from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class AbtractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    GENDER_CHOICE = [
        ('m', 'Male'),
        ('f', 'Female'),
    ]

    age = models.IntegerField(null=True)
    address = models.TextField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE, null=True)

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


# Create your models here


class LawyerSignup(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    email = models.EmailField(max_length=250, unique=True)
    mobile = models.PositiveIntegerField(validators=[MinLengthValidator(10), MaxLengthValidator(10)])
    age = models.IntegerField()
    exp = models.IntegerField()
    language = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    picture = models.FileField(upload_to="profile_images/", blank=False, default='generic-user-purple.jpg')
    degree = models.FileField(upload_to='Degree')
    certificate = models.FileField(upload_to='Certificate')

    def __str__(self):
        return self.email


class Signup(models.Model):
    username = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250, unique=True)
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.email


class Contact(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=250)
    Subject = models.CharField(max_length=50)

    def __str__(self):
        return self.Email


class Talk_to_lawyer(models.Model):
    Area = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Email = models.EmailField(max_length=250)
    Subject = models.CharField(max_length=50)
    Lawyer = models.CharField(max_length=100)

    def __str__(self):
        return self.Email

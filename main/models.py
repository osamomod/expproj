from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Profile(models.Model):
    name = models.CharField(max_length=100)
    experience = models.TextField()
    qualifications = models.TextField()
    about = models.TextField()
    photo = models.ImageField(upload_to="profile_photos/")
    phone = models.CharField(max_length=15, default="Телефон не указан")
    email = models.EmailField(default="Почта не указан")
    address = models.CharField(max_length=255, default="Адрес не указан")

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    client_phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.client_name} - {self.service.name}"


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    rating = models.IntegerField()
    comment = models.TextField()
    image = models.ImageField(
        upload_to="review_images/", blank=True, null=True
    )  # Добавил null=True
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.rating}"

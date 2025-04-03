from django.contrib.auth.models import AbstractUser
from django.db import models

class DishType(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Ingredient(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=10
    )
    dish_type = models.ForeignKey(
        DishType,
        on_delete=models.CASCADE,
        related_name="dish_type",
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name="ingredients",
        blank=True
    )
    cooks = models.ManyToManyField(
        Cook,
        blank=True,
        related_name="dishes",
    )

    def __str__(self):
        return f"{self.name} ({self.dish_type}): {self.price}"
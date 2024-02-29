from django.db import models
from django.contrib.auth.models import User


class RecipeModel(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=1000)
    tags = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title}, {self.description}"

    class Meta:
        ordering = ['title']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user


class Ingredients(models.Model):
    ingredient = models.CharField(max_length=200, blank=True)
    recipe = models.ManyToManyField(RecipeModel)

    def __str__(self) -> str:
        return f"{self.ingredient}"
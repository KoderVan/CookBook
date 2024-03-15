from django.contrib import admin
from .models import RecipeModel,RecipeIngredients

admin.site.register(RecipeIngredients)
admin.site.register(RecipeModel)

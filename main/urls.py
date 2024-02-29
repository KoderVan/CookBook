from django.urls import path
from .views import (RegistrationForm, CustomLoginForm, RecipeView, CreateRecipe, RecipeList, logged_out, ProfileView,
                    HomePage, AddIngredient)
from . import views


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('register/', RegistrationForm.as_view(), name='register'),
    path('login/', CustomLoginForm.as_view(), name='login'),
    path('logout/', views.logged_out, name='logout'),
    path('profile<int:pk>/', ProfileView.as_view(), name='profile'),
    path('recipe<int:pk>/', RecipeView.as_view(), name='recipe'),
    path('create/', CreateRecipe.as_view(), name='create'),
    path('recipe-list/', RecipeList.as_view(), name='recipe-list'),
    path('add-ing<int:pk>/', AddIngredient.as_view(), name='add'),
]

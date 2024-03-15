from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView, UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from .models import RecipeModel, Profile, RecipeIngredients, Ingredient
from django.db import models


class RegistrationForm(FormView):
    form_class = UserCreationForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            redirect('home')
        return super(RegistrationForm, self).form_valid(form)


class CustomLoginForm(LoginView):
    form = LoginView
    template_name = 'main/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


def logged_out(request):
    logout(request)
    return render(request, 'main/logout.html', context={})


class HomePage(ListView):
    model = RecipeModel
    context_object_name = 'home'
    template_name = 'main/home.html'


class RecipeList(ListView):
    model = RecipeModel
    context_object_name = 'recipelist'
    template_name = 'main/recipe-list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context[RecipeList.context_object_name] = context[RecipeList.context_object_name].objects.filter(title_startswith=search_input)
        return context


class RecipeView(DetailView):
    model = RecipeModel
    context_object_name = 'recipe'
    fields = ['title', 'description', 'tags']
    template_name = 'main/recipe.html'

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe_id'] = RecipeIngredients.objects.filter(recipe_id=self.object) 
        context['ingredients'] = context['recipe_id']
        return context       


class CreateRecipe(CreateView):
    model = RecipeModel
    context_object_name = 'create'
    fields = ['title', 'description', 'tags']
    template_name = 'main/create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateRecipe, self).form_valid(form)


class AddIngredient(CreateView):
    model = RecipeIngredients
    context_object_name = 'new-ingredient'
    fields = ['ingredient', 'count','units']
    template_name = 'main/new-ingredient.html'
    success_url = reverse_lazy('recipe-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = self.request.GET.get('id')
        return context
    
    def form_valid(self, form):
        return super(AddIngredient, self).form_valid(form)


class ProfileView(DetailView):
    model = Profile
    template_name = 'main/profile.html'

    def get_context_data(self, **kwargs):
        users = Profile.objects.all()
        context = super(ProfileView, self).get_context_data(**kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


from django.shortcuts import render
from django.views import generic

from menu.models import Dish, DishType, Cook, Ingredient


def index(request):

    num_dishes = Dish.objects.count()
    num_cooks = Cook.objects.count() - 1

    context = {
        'num_dishes': num_dishes,
        'num_cooks': num_cooks,
    }

    return render(request, "menu/home.html", context)


class DishListView(generic.ListView):
    model = Dish
    queryset = Dish.objects.all()
    context_object_name = "dishes_list"
    template_name = "menu/dish_list.html"


class CookListView(generic.ListView):
    model = Cook
    queryset = Cook.objects.all()
    context_object_name = "cooks_list"
    template_name = "menu/cook_list.html"


class IngredientListView(generic.ListView):
    model = Ingredient
    queryset = Ingredient.objects.all()
    context_object_name = "ingredients_list"
    template_name = "menu/ingredient_list.html"


class DishTypeListView(generic.ListView):
    model = DishType
    queryset = DishType.objects.all()
    context_object_name = "dish_types_list"
    template_name = "menu/dish_type_list.html"


class DishDetailView(generic.DetailView):
    model = Dish
    template_name = "menu/dish_detail.html"
    context_object_name = "dish"


class CookDetailView(generic.DetailView):
    model = Cook
    template_name = "menu/cook_detail.html"
    context_object_name = "cook"

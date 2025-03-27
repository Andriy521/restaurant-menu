from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from menu.forms import CookCreationForm

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
    paginate_by = 5


class DishDetailView(generic.DetailView):
    model = Dish
    template_name = "menu/dish_detail.html"
    context_object_name = "dish"


class DishCreateView(generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("dishes-list")


class DishUpdateView(generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("dishes-list")


class DishDeleteView(generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("dishes-list")


class CookListView(generic.ListView):
    model = Cook
    queryset = Cook.objects.all()
    context_object_name = "cooks_list"
    template_name = "menu/cook_list.html"
    paginate_by = 5


class CookDetailView(generic.DetailView):
    model = Cook
    template_name = "menu/cook_detail.html"
    context_object_name = "cook"


class CookCreateView(generic.CreateView):
    model = Cook
    form_class = CookCreationForm


class CookDeleteView(generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("cooks-list")


class IngredientListView(generic.ListView):
    model = Ingredient
    queryset = Ingredient.objects.all()
    context_object_name = "ingredients_list"
    template_name = "menu/ingredient_list.html"
    paginate_by = 5


class IngredientCreateView(generic.CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("ingredients-list")


class IngredientUpdateView(generic.UpdateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("ingredients-list")


class IngredientDeleteView(generic.DeleteView):
    model = Ingredient
    success_url = reverse_lazy("ingredients-list")


class DishTypeListView(generic.ListView):
    model = DishType
    queryset = DishType.objects.all()
    context_object_name = "dish_types_list"
    template_name = "menu/dish_type_list.html"
    paginate_by = 5


class DishTypeCreateView(generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("types-list")


class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("types-list")


class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("types-list")



def dish_list_by_ingredient(request, ingredient_id):
    ingredient = Ingredient.objects.get(id=ingredient_id)
    dishes = Dish.objects.filter(ingredients=ingredient)

    context = {
        'ingredient': ingredient,
        'dishes': dishes
    }

    return render(request, 'menu/dish_list_by_ingredient.html', context)

def dish_list_by_type(request, type_id):
    dish_type = DishType.objects.get(id=type_id)
    dishes = Dish.objects.filter(dish_type=dish_type)

    context = {
        'dish_type': dish_type,
        'dishes': dishes
    }

    return render(request, 'menu/dish_list_by_dish_type.html', context)


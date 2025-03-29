from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from menu.forms import CookCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from menu.models import Dish, DishType, Cook, Ingredient


def index(request):

    num_dishes = Dish.objects.count()
    num_cooks = Cook.objects.count() - 1

    context = {
        'num_dishes': num_dishes,
        'num_cooks': num_cooks,
    }

    return render(request, "menu/home.html", context)


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    context_object_name = "dishes_list"
    template_name = "menu/dishes_list.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = Dish.objects.all()
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    template_name = "menu/dish_detail.html"
    context_object_name = "dish"


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("dishes-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("dishes-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("dishes-list")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    context_object_name = "cooks_list"
    template_name = "menu/cook_list.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = Cook.objects.all()
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(username__icontains=query)
        return queryset


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    template_name = "menu/cook_detail.html"
    context_object_name = "cook"


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy("cooks-list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("cooks-list")


class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    context_object_name = "ingredients_list"
    template_name = "menu/ingredient_list.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = Ingredient.objects.all()
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("ingredients-list")


class IngredientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("ingredients-list")


class IngredientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ingredient
    success_url = reverse_lazy("ingredients-list")


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    queryset = DishType.objects.all()
    context_object_name = "dish_types_list"
    template_name = "menu/dish_type_list.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = DishType.objects.all()
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("types-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("types-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("types-list")


class DishListByIngredientView(LoginRequiredMixin, generic.ListView):
    model = Dish
    template_name = 'menu/dish_list_by_ingredient.html'
    context_object_name = 'dishes'

    def get_queryset(self):
        ingredient = Ingredient.objects.get(id=self.kwargs['ingredient_id'])
        return Dish.objects.filter(ingredients=ingredient)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredient'] = Ingredient.objects.get(id=self.kwargs['ingredient_id'])
        return context


class DishListByTypeView(LoginRequiredMixin, generic.ListView):
    model = Dish
    template_name = 'menu/dish_list_by_dish_type.html'
    context_object_name = 'dishes'

    def get_queryset(self):
        dish_type = DishType.objects.get(id=self.kwargs['type_id'])
        return Dish.objects.filter(dish_type=dish_type)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dish_type'] = DishType.objects.get(id=self.kwargs['type_id'])
        return context

"""
URL configuration for restaurant_menu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from menu.views import (
    index,
    DishListView,
    CookListView,
    IngredientListView,
    DishTypeListView,
    DishDetailView,
    CookDetailView,
    dish_list_by_ingredient,
    CookCreateView,
    CookDeleteView,
    dish_list_by_type,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    IngredientCreateView,
    IngredientUpdateView,
    IngredientDeleteView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="home"),
    path("dishes/", DishListView.as_view(), name="dishes-list"),
    path("dishes/create/", DishCreateView.as_view(), name="dishes-create"),
    path("dishes/update/<int:pk>", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/delete/<int:pk>", DishDeleteView.as_view(), name="dish-delete"),
    path("cooks/", CookListView.as_view(), name="cooks-list"),
    path("cooks/create/", CookCreateView.as_view(), name="cooks-create"),
    path("cooks/delete/<int:pk>/", CookDeleteView.as_view(), name="cooks-delete"),
    path("ingredients/", IngredientListView.as_view(), name="ingredients-list"),
    path("ingredients/create/", IngredientCreateView.as_view(), name="ingredients-create"),
    path("ingredients/update/<int:pk>/", IngredientUpdateView.as_view(), name="ingredients-update"),
    path("ingredients/delete/<int:pk>/", IngredientDeleteView.as_view(), name="ingredients-delete"),
    path("ingredients/<int:ingredient_id>/dishes/", dish_list_by_ingredient, name='dish-list-by-ingredient'),
    path("types/<int:type_id>/dishes/", dish_list_by_type, name='dish-list-by-type'),
    path("types/", DishTypeListView.as_view(), name="types-list"),
    path("types/create/", DishTypeCreateView.as_view(), name="types-create"),
    path("types/update/<int:pk>/", DishTypeUpdateView.as_view(), name="types-update"),
    path("types/delete/<int:pk>/", DishTypeDeleteView.as_view(), name="types-delete"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
]

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
    dish_list_by_ingredient
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="home"),
    path("dishes/", DishListView.as_view(), name="dishes-list"),
    path("cooks/", CookListView.as_view(), name="cooks-list"),
    path("ingredients/", IngredientListView.as_view(), name="ingredients-list"),
    path("ingredient/<int:ingredient_id>/dishes/", dish_list_by_ingredient, name='dish-list-by-ingredient'),
    path("types/", DishTypeListView.as_view(), name="types-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
]

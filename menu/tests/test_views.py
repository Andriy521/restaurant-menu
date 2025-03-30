from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from menu.models import DishType, Ingredient, Dish


class PublicDishTypeTests(TestCase):
    def test_login_required(self):
        res = self.client.get(reverse("types-list"))

        self.assertNotEqual(res.status_code, 200)


class PrivateDishTypeTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)
        DishType.objects.create(name="biscuit")
        DishType.objects.create(name="drink")

    def test_retrieve_dish_types(self):
        res = self.client.get(reverse("types-list"))
        self.assertEqual(res.status_code, 200)
        dish_types = DishType.objects.all()
        self.assertEqual(list(res.context["dish_types_list"]), list(dish_types))
        self.assertTemplateUsed(res,"menu/dish_type_list.html")


class PublicIngredientTests(TestCase):
    def test_login_required(self):
        res = self.client.get(reverse("ingredients-list"))

        self.assertNotEqual(res.status_code, 200)


class PrivateIngredientTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)
        Ingredient.objects.create(name="potato")
        Ingredient.objects.create(name="cheese")

    def test_retrieve_dish_types(self):
        res = self.client.get(reverse("ingredients-list"))
        self.assertEqual(res.status_code, 200)
        dish_types = Ingredient.objects.all()
        self.assertEqual(list(res.context["ingredients_list"]), list(dish_types))
        self.assertTemplateUsed(res,"menu/ingredient_list.html")


class PublicCookTests(TestCase):
    def test_login_required(self):
        res = self.client.get(reverse("cooks-list"))

        self.assertNotEqual(res.status_code, 200)


class PrivateCookTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_types(self):
        get_user_model().objects.create(username="test1",
                                        password="<PASSWORD>")

        res = self.client.get(reverse("cooks-list"))
        self.assertEqual(res.status_code, 200)
        cooks = get_user_model().objects.all()
        self.assertEqual(list(res.context["cooks_list"]), list(cooks))
        self.assertTemplateUsed(res,"menu/cook_list.html")


class PublicDishTests(TestCase):
    def test_login_required(self):
        res = self.client.get(reverse("dishes-list"))

        self.assertNotEqual(res.status_code, 200)


class PrivateDishTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)
        dish_type = DishType.objects.create(name="test")
        carbonara = Dish.objects.create(
            name="Pasta Carbonara",
            price=10.99,
            dish_type=dish_type
        )
        pizza = Dish.objects.create(
            name="Margherita Pizza",
            price=8.99,
            dish_type=dish_type
        )
        salad = Dish.objects.create(
            name="Caesar Salad",
            price=6.99,
            dish_type=dish_type
        )

    def test_retrieve_dish_types(self):
        res = self.client.get(reverse("dishes-list"))
        self.assertEqual(res.status_code, 200)
        dishes = Dish.objects.all()
        self.assertEqual(list(res.context["dishes_list"]), list(dishes))
        self.assertTemplateUsed(res,"menu/dishes_list.html")

    def test_get_queryset_no_filter(self):
        res = self.client.get(reverse("dishes-list"))
        dishes = Dish.objects.all()
        self.assertEqual(list(res.context["dishes_list"]), list(dishes))

    def test_get_queryset_with_filter(self):
        res = self.client.get(reverse("dishes-list"), {"query": "Pizza"})
        filtered_dishes = Dish.objects.filter(name__icontains="Pizza")
        self.assertEqual(list(res.context["dishes_list"]), list(filtered_dishes))
from django.test import TestCase

from menu.models import Cook, Dish, DishType, Ingredient

class ModelsTest(TestCase):
    def test_cook_str(self):
        cook = Cook.objects.create_user(
            username="test",
            password="test123",
            first_name="test_first_name",
            last_name="test_last_name",
        )

        self.assertEqual(str(cook),
                         f"{cook.username} ({cook.first_name} {cook.last_name})")

    def test_dish_str(self):
        dish_type = DishType.objects.create(
            name="test_dish_type",
        )
        dish = Dish.objects.create(
            name="test_dish",
            price=100,
            dish_type=dish_type,
        )

        self.assertEqual(str(dish),
                         f"{dish.name} ({dish.dish_type.name}): {dish.price}")

    def test_ingredient_str(self):
        ingredient = Ingredient.objects.create(
            name="test_ingredient",
        )
        self.assertEqual(str(ingredient),
                        ingredient.name)

    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="test_dish_type",
        )

        self.assertEqual(str(dish_type),
                         dish_type.name)

    def test_create_cook_with_years_of_experience(self):
        cook = Cook.objects.create_user(
            username="test",
            password="test123",
            years_of_experience=10,
        )

        self.assertEqual(cook.username, "test")
        self.assertEqual(cook.years_of_experience, 10)
        self.assertTrue(cook.check_password("test123"))


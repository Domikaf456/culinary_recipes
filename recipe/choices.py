EASY = 'Łatwa'
MEDIUM = 'Średnia'
HARD = 'Trudna'

DIFFICULTY_CHOICES = [
    (EASY, 'Łatwa'),
    (MEDIUM, 'Średnia'),
    (HARD, 'Trudna'),
]

BREAKFAST = "Śniadanie"
LUNCH = "Obiad"
DINNER = "Kolacja"

TYPE_OF_MEAL_CHOICES = [
    (BREAKFAST, 'Śniadanie'),
    (LUNCH, 'Obiad'),
    (DINNER, 'Kolacja')
]

VEGETARIAN = 'Wegetariańskie'
VEGAN = 'Wegańskie'
MEAT = 'Mięsne'
FISH = 'Rybne'

CATEGORY_CHOICES = [
    (VEGETARIAN, 'Wegetariańskie'),
    (VEGAN, 'Wegańskie'),
    (MEAT, 'Mięsne'),
    (FISH, 'Rybne')
]

LACTOSE_FREE = "Bez laktozy"
GLUTEN_FREE = "Bez glutenu"
DAIRY_FREE = "Bez mleka"
VEGETARIAN_OR_VEGAN = "Wegetariańskie"
MEAT = "Mięsne"
FISH = "Rybne"

LACTOSE_CHOICES = [
    ('', '---'),
    (LACTOSE_FREE, 'Bez laktozy'),
]

GLUTEN_CHOICES = [
    ('', '---'),
    (GLUTEN_FREE, 'Bez glutenu'),
]

DAIRY_CHOICES = [
    ('', '---'),
    (DAIRY_FREE, 'Bez mleka'),
]

VEGETARIAN_VEGAN_CHOICES = [
    ('', '---'),
    (VEGETARIAN_OR_VEGAN, 'Wegetariańskie'),
    (VEGETARIAN_OR_VEGAN, 'Wegańskie'),
]

MEAT_CHOICES = [
    ('', '---'),
    (MEAT, 'Mięsne'),
]

FISH_CHOICES = [
    ('', '---'),
    (FISH, 'Rybne'),
]
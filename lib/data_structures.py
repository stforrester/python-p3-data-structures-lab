spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [dict.get("name") for dict in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [dict for dict in spicy_foods if (dict.get("heat_level") > 5)]

def print_spicy_foods(spicy_foods):
    for dict in spicy_foods:
        print(f"{dict.get('name')} ({dict.get('cuisine')}) | Heat Level: {dict.get('heat_level')*'🌶'}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    list = [dict for dict in spicy_foods if dict.get("cuisine") == cuisine]
    return list[0]

def print_spiciest_foods(spicy_foods):
    for dict in spicy_foods:
        if dict.get("heat_level") > 5:
            print(f"{dict.get('name')} ({dict.get('cuisine')}) | Heat Level: {dict.get('heat_level')*'🌶'}")

def get_average_heat_level(spicy_foods):
    heat_level = 0
    for dict in spicy_foods:
        heat_level += dict.get("heat_level")
    return heat_level / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

def validate_ingredients(ingredients: str) -> str:
    ingredients = ingredients.split(" ")
    for ingredient in ingredients:
        if (
            ingredient == "fire" or
            ingredient == "water" or
            ingredient == "earth" or
            ingredient == "air"
        ):
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"

def format_ingredients(ingredients):
    if len(ingredients) > 2:
        return ", ".join(ingredients[:-1]) + " and " + ingredients[-1]
    else:
        return " and ".join(ingredients)

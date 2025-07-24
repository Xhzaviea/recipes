def recipe_organizer(recipes):
    user_input = input("Enter ingredients you have, separated by commas: ")
    ingredients = [item.strip().lower() for item in user_input.split(",")]

    matches = {}

    for meal, required in recipes.items():
       common = set(ingredients) & set(required)
       if len(common) >= 2:  # at least 2 matching ingredients
        matches[meal] = list(common)
       if matches:
          print("\nBased on your ingredients, you can make:")
    for meal, matched_items in matches.items():
        print(f"- {meal} (matches: {', '.join(matched_items)})")
    else:
           print("Hmm... No recipes match. Try entering more ingredients!")
    favorites = []

    save = input("Would you like to save one of these recipes as a favorite? (yes/no): ").lower()
    if save == "yes":
     chosen = input("Type the name of the recipe to save: ").strip()
     if chosen in matches:
         favorites.append(chosen)
         print(f"{chosen} has been added to your favorites.")
    view = input("Do you want to view your favorites? (yes/no): ").lower()
    if view == "yes":
        print(" Your favorite recipes:")
        for fav in favorites:
            fav = ("chosen")
        print(f"- {fav}")

sample_recipes = {
    "Pasta Salad": ["pasta", "tomato", "cucumber", "olive oil"],
    "Fruit Smoothie": ["banana", "milk", "honey"],
    "Omelette": ["egg", "onion", "tomato"],
    "Avocado Toast": ["bread", "avocado", "salt"],
    "Pancakes": ["flour", "milk", "egg", "sugar"],
}
recipe_organizer(sample_recipes)

import requests

# Function to fetch recipes from the API based on user input
def fetch_recipes(ingredient):
    url = f"https://example-recipe-api.com/recipes?ingredient={ingredient}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to filter recipes based on dietary preferences
def filter_recipes_by_diet(recipes, diet_preference):
    return [recipe for recipe in recipes if recipe['diet'] == diet_preference]

# Function to display the recipes
def display_recipes(recipes):
    if not recipes:
        print("No recipes found for this ingredient.")
    else:
        print("Here are the matching recipes:")
        for index, recipe in enumerate(recipes, 1):
            print(f"{index}. {recipe['name']} - {recipe['diet']}")

# Main function to run the recipe finder application
def main():
    print("Welcome to the Recipe Finder!")
    ingredient = input("Enter an ingredient to search for recipes: ")

    recipes = fetch_recipes(ingredient)
    if not recipes:
        print("Sorry, could not fetch recipes at the moment. Please try again later.")
        return

    diet_preference = input("Do you have any dietary preferences? (Vegan/Vegetarian/Non-vegetarian): ")
    filtered_recipes = filter_recipes_by_diet(recipes, diet_preference.lower())

    display_recipes(filtered_recipes)

if __name__ == "__main__":
    main()


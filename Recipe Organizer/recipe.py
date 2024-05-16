import json

class RecipeOrganizer:
    def __init__(self):
        self.recipes = {}
        self.load_recipes()

    def load_recipes(self):
        try:
            with open('recipes.json', 'r') as file:
                self.recipes = json.load(file)
        except FileNotFoundError:
            self.recipes = {}

    def save_recipes(self):
        with open('recipes.json', 'w') as file:
            json.dump(self.recipes, file, indent=4)

    def add_recipe(self):
        name = input("Enter the recipe name: ")
        ingredients = input("Enter the ingredients (comma separated): ").split(',')
        instructions = input("Enter the cooking instructions: ")

        self.recipes[name] = {
            'ingredients': [ingredient.strip() for ingredient in ingredients],
            'instructions': instructions
        }
        self.save_recipes()
        print(f'Recipe for {name} added successfully.')

    def view_recipe(self):
        name = input("Enter the recipe name to view: ")
        if name in self.recipes:
            print(f"Recipe for {name}:")
            print("Ingredients:")
            for ingredient in self.recipes[name]['ingredients']:
                print(f"- {ingredient}")
            print("Instructions:")
            print(self.recipes[name]['instructions'])
        else:
            print("Recipe not found.")

    def search_recipes(self):
        search_term = input("Enter a keyword to search for: ")
        found_recipes = [name for name in self.recipes if search_term.lower() in name.lower()]
        if found_recipes:
            print("Recipes found:")
            for name in found_recipes:
                print(f"- {name}")
        else:
            print("No recipes found.")

    def create_shopping_list(self):
        selected_recipes = input("Enter the names of the recipes (comma separated): ").split(',')
        shopping_list = []
        for name in selected_recipes:
            if name.strip() in self.recipes:
                shopping_list.extend(self.recipes[name.strip()]['ingredients'])
            else:
                print(f"Recipe for {name.strip()} not found.")
        if shopping_list:
            print("Shopping List:")
            for item in set(shopping_list):
                print(f"- {item}")

    def menu(self):
        while True:
            print("\nRecipe Organizer")
            print("1. Add Recipe")
            print("2. View Recipe")
            print("3. Search Recipes")
            print("4. Create Shopping List")
            print("5. Exit")

            choice = input("Choose an option: ")
            if choice == '1':
                self.add_recipe()
            elif choice == '2':
                self.view_recipe()
            elif choice == '3':
                self.search_recipes()
            elif choice == '4':
                self.create_shopping_list()
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    organizer = RecipeOrganizer()
    organizer.menu()

class Recipe:
    def __init__(self, name, ingredients, cuisine, allergies):
        self.name = name
        self.ingredients = ingredients
        self.cuisine = cuisine
        self.allergies = allergies

class RecipeRecommendationSystem:
    def __init__(self, recipes):
        self.recipes = recipes

    def get_recommendations(self, user_preferences):
        """
        Get recipe recommendations based on user preferences.

        :param user_preferences: A dictionary containing user preferences.
        :return: A list of recommended recipes.
        """
        recommendations = []

        for recipe in self.recipes:
            # Check if the recipe matches user preferences
            if self.check_preferences(recipe, user_preferences):
                recommendations.append(recipe)

        return recommendations

    def check_preferences(self, recipe, user_preferences):
        """
        Check if a recipe matches user preferences.

        :param recipe: The recipe to check.
        :param user_preferences: A dictionary containing user preferences.
        :return: True if the recipe matches user preferences, False otherwise.
        """
        # Check cuisine preference
        if 'cuisine' in user_preferences and recipe.cuisine != user_preferences['cuisine']:
            return False

        # Check allergies
        if 'allergies' in user_preferences and any(allergy in recipe.allergies for allergy in user_preferences['allergies']):
            return False

        # Check ingredients availability
        if 'ingredients' in user_preferences and not all(ingredient in recipe.ingredients for ingredient in user_preferences['ingredients']):
            return False

        return True

# Sample recipes
recipes = [
    Recipe("Spaghetti Bolognese", ["spaghetti", "ground beef", "tomato sauce"], "Italian", ["gluten"]),
    Recipe("Chicken Stir-Fry", ["chicken", "vegetables", "soy sauce"], "Asian", []),
    Recipe("Caprese Salad", ["tomatoes", "mozzarella", "basil"], "Italian", ["dairy"]),
    # Add more recipes as needed
]

# Sample user preferences
user_preferences = {
    'cuisine': 'Italian',
    'allergies': ['dairy'],
    'ingredients': ['tomatoes', 'basil']
}

# Create a recipe recommendation system
recommendation_system = RecipeRecommendationSystem(recipes)

# Get recipe recommendations based on user preferences
recommendations = recommendation_system.get_recommendations(user_preferences)

# Print the recommendations
print("Recommended Recipes:")
for recipe in recommendations:
    print(recipe.name)

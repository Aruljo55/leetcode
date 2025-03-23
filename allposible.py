from collections import defaultdict

class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        # Create a set of supplies for quick lookup
        supply_set = set(supplies)
        # Create a dictionary to store ingredients for each recipe
        recipe_ingredients = defaultdict(list)
        
        # Store the ingredients required for each recipe
        for i in range(len(recipes)):
            recipe_ingredients[recipes[i]] = ingredients[i]
        
        # A set to keep track of which recipes we can create
        can_create = set()

        def dfs(recipe):
            if recipe in can_create:
                return True  # Already known to be creatable
            
            # If the recipe can be made from available supplies, add it to can_create
            if recipe in supply_set:
                can_create.add(recipe)
                return True
            
            # Otherwise, check if all the ingredients for the recipe can be created
            all_ingredients_available = True
            for ingredient in recipe_ingredients[recipe]:
                if ingredient not in can_create and not dfs(ingredient):
                    all_ingredients_available = False
                    break
            
            if all_ingredients_available:
                can_create.add(recipe)
                return True
            return False

        # Try to make each recipe
        for recipe in recipes:
            dfs(recipe)
        
        return list(can_create)

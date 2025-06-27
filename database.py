import sqlite3
import json # Optional: for pretty printing the initial data, not strictly for DB saving

# --- Your Recipe Data (as provided previously) ---
recipes = {
    "Cookies": [
        {
            "name": "Base Cookie Recipe",
            "ingredients": [
                "2 1/2 cups flour",
                "2 cups melted butter",
                "1 1/2 cups brown sugar",
                "1/2 tsp salt",
                "1 tsp baking soda",
                "1 egg yolk, room temperature",
                "1 whole egg, room temperature"
            ],
            "instructions": [
                "Measure all the ingredients.",
                "Mix the melted butter with the brown sugar.",
                "In a separate bowl, combine the flour, salt, and baking soda.",
                "Incorporate the egg and egg yolk into the butter and sugar mixture.",
                "Gradually combine all ingredients together.",
                "Portion the dough into individual cookies and freeze overnight.",
                "When you’re craving a cookie, bake the frozen dough straight from the freezer at 350°F for 15 minutes."
            ]
        },
        {
            "name": "Double Walnut Chocolate Chip Cookies",
            "ingredients": [
                "2 cups flour",
                "1/2 cup cocoa powder",
                "10 oz chocolate chips",
                "1 cup chopped walnuts",
                "2 cups melted butter",
                "1 1/2 cups brown sugar",
                "1/2 tsp salt",
                "1 tsp baking soda",
                "1 egg yolk, room temperature",
                "1 whole egg, room temperature"
            ],
            "instructions": [
                "Measure all ingredients, treating the cocoa powder as you would flour.",
                "Mix the melted butter with the brown sugar.",
                "In a separate bowl, combine the flour, cocoa powder, salt, baking soda, and walnuts.",
                "Incorporate the egg and egg yolk into the butter and sugar mixture.",
                "Gradually combine all ingredients together.",
                "Portion the dough into individual cookies and freeze overnight.",
                "When you’re ready for a cookie, bake the frozen dough straight from the freezer at 350°F for 15 minutes."
            ]
        },
        {
            "name": "Strawberry Matcha Cookies",
            "ingredients": [
                "2 cups flour",
                "1/2 cup matcha powder",
                "8 strawberries",
                "2 cups melted butter",
                "1 cup brown sugar",
                "1/2 cup maple syrup",
                "1/2 tsp salt",
                "1 tsp baking soda",
                "1 egg yolk, room temperature",
                "1 whole egg, room temperature"
            ],
            "instructions": [
                "Measure all ingredients, treating the matcha powder as you would flour.",
                "Mix the melted butter with the brown sugar.",
                "In a separate bowl, combine the flour, matcha powder, salt, and baking soda.",
                "Blend 6 strawberries with the egg yolk and whole egg.",
                "Incorporate the strawberry-egg mixture into the flour mixture, and then add the maple syrup.",
                "Combine all ingredients thoroughly and portion the dough into individual cookies.",
                "Slice the remaining strawberries and place one slice on top of each cookie. Freeze overnight.",
                "When you’re ready to bake, cook the frozen cookies straight from the freezer at 350°F for 15 minutes."
            ]
        },
        {
            "name": "Oatmeal Raisin Cookie",
            "ingredients": [
                "1/2 cup butter",
                "1 cup brown sugar",
                "1/2 tsp salt",
                "1 cup raisins",
                "1/2 tsp cinnamon",
                "1/2 tsp nutmeg",
                "1/2 tsp cardamom",
                "1 tsp baking soda",
                "1 egg yolk, room temperature",
                "1 whole egg, room temperature",
                "3 cups oats"
            ],
            "instructions": [
                "Measure all ingredients.",
                "In a bowl, combine oats, salt, cinnamon, nutmeg, cardamom, raisins, and baking soda.",
                "Mix the melted butter with the brown sugar.",
                "Incorporate the egg and egg yolk into the butter-sugar mixture.",
                "Gradually add the oat mixture into the wet ingredients and combine everything together.",
                "Portion the dough into individual cookies and freeze overnight.",
                "When you’re ready to bake, place the frozen cookies straight from the freezer onto a baking sheet and bake at 350°F for 15 minutes."
            ]
        },
        {
            "name": "Black Sesame Black Tea Walnut Crumble Cookie",
            "ingredients": [
                "2 1/2 cups flour",
                "1/2 cup black sesame powder",
                "2 cups ghee",
                "1 cup chopped walnuts",
                "1 1/2 cups brown sugar",
                "1/2 tsp salt",
                "1 tsp baking soda",
                "1 egg yolk, room temperature",
                "1 whole egg, room temperature",
                "8 tea bags"
            ],
            "instructions": [
                "Infuse the ghee with the 8 tea bags for 8 hours, then mix the infused ghee with the brown sugar.",
                "Measure all ingredients.",
                "In a separate bowl, combine the flour, salt, walnuts, black sesame powder, and baking soda.",
                "Incorporate the egg and egg yolk into the ghee-sugar mixture.",
                "Gradually add the dry ingredients to the wet mixture and combine everything together.",
                "Portion the dough into individual cookies and freeze overnight.",
                "When you’re ready to bake, place the frozen cookies straight from the freezer onto a baking sheet and bake at 350°F for 15 minutes."
            ]
        },
        {
            "name": "Tangerine Cookie",
            "ingredients": [
                "2 1/2 cups flour",
                "1 tangerine",
                "2 cups melted butter",
                "1 cup brown sugar",
                "1/2 cup honey",
                "1/2 tsp salt",
                "1 tsp baking soda",
                "1 egg yolk, room temperature",
                "1 whole egg, room temperature"
            ],
            "instructions": [
                "Measure all ingredients.",
                "Juice and zest the tangerine.",
                "In a bowl, combine the flour, tangerine zest, salt, and baking soda.",
                "Mix the melted butter with the brown sugar.",
                "In a separate bowl, mix the tangerine juice with the egg yolk and whole egg.",
                "Incorporate the tangerine-egg mixture into the butter and sugar mixture.",
                "Gradually add the dry ingredients to the wet mixture and combine everything together.",
                "Portion the dough into individual cookies and freeze.",
                "When you’re ready for a cookie, bake the frozen dough straight from the freezer at 350°F for 15 minutes."
            ]
        },
        {
            "name": "Earl Grey Orange Cookies",
            "ingredients": [
                "2 1/2 cups flour",
                "1 orange",
                "2 cups ghee",
                "1 1/2 cups brown sugar",
                "1/2 tsp salt",
                "1 tsp baking soda",
                "1 egg yolk, room temperature",
                "1 whole egg, room temperature",
                "8 Earl Grey tea bags"
            ],
            "instructions": [
                "Infuse the ghee with the Earl Grey tea bags for 8 hours, then mix the infused ghee with the brown sugar.",
                "Measure all ingredients.",
                "Juice and zest the orange.",
                "In a bowl, combine the flour, orange zest, salt, and baking soda.",
                "Mix the orange juice with the egg yolk and whole egg.",
                "Incorporate the orange-egg mixture into the flour mixture.",
                "Combine all ingredients and portion the dough into individual cookies.",
                "Freeze the cookies overnight.",
                "When ready to bake, bake the frozen cookies straight from the freezer at 350°F for 15 minutes."
            ]
        },
        {
            "name": "Chamomile Lavender Lemon Cookie",
            "ingredients": [
                "2 1/2 cups flour",
                "1 lemon",
                "2 cups ghee",
                "1 1/2 cups brown sugar",
                "1/2 tsp salt",
                "1 tsp baking soda",
                "1 egg yolk, room temperature",
                "1 whole egg, room temperature",
                "8 Chamomile Lavender tea bags"
            ],
            "instructions": [
                "Infuse the ghee with the Chamomile Lavender tea bags for 8 hours, then mix the infused ghee with the brown sugar.",
                "Measure all ingredients.",
                "Juice and zest the lemon.",
                "In a bowl, combine the flour, lemon zest, salt, and baking soda.",
                "Mix the lemon juice with the egg yolk and whole egg.",
                "Incorporate the lemon-egg mixture into the flour mixture.",
                "Combine all ingredients and portion the dough into individual cookies.",
                "Freeze the cookies overnight.",
                "When ready to bake, bake the frozen cookies straight from the freezer at 350°F for 15 minutes."
            ]
        }
    ],
    "Fried Chicken": [
        {
            "name": "Base Fried Chicken Recipe",
            "ingredients": [
                "1 teaspoon baking soda",
                "1/4 cup water",
                "Chicken",
                "Salt",
                "Pepper"
            ],
            "instructions": [
                "In a closed container, marinate the chicken for 2 hours in the refrigerator with 1 teaspoon of baking soda and 1/4 cup water.",
                "After 2 hours, rinse off the baking soda and marinade the chicken for 1 hour with the spice mix (salt, pepper).",
                "Wings/Drumsticks: Air fry for 24 minutes at 400°F. Flip halfway through for extra crispiness.",
                "Chicken Breast: Air fry for 16 minutes at 400°F.",
                "Chicken Cutlets: Air fry for 15 minutes at 400°F."
            ]
        },
        {
            "name": "Cornstarch Fried Chicken Wings",
            "ingredients": [
                "1 teaspoon baking soda",
                "1/4 cup water",
                "Chicken",
                "1 teaspoon vegetable oil",
                "1 teaspoon cooking wine",
                "1 teaspoon oyster sauce",
                "1 teaspoon soy sauce",
                "2 teaspoon cornstarch"
            ],
            "instructions": [
                "In a closed container, marinate the chicken for 2 hours in the refrigerator with 1 teaspoon of baking soda and 1/4 cup water.",
                "After 2 hours, rinse off the baking soda and marinade the chicken for 1 hour with the spice mix (vegetable oil, cooking wine, oyster sauce, soy sauce, cornstarch).",
                "Wings/Drumsticks: Air fry for 24 minutes at 400°F. Flip halfway through for extra crispiness.",
                "Chicken Breast: Air fry for 16 minutes at 400°F.",
                "Chicken Cutlets: Air fry for 15 minutes at 400°F."
            ]
        },
        {
            "name": "Fried Chicken Katsu",
            "ingredients": [
                "1 teaspoon baking soda",
                "1/4 cup water",
                "Panko bread crumbs",
                "1 egg",
                "Flour",
                "6 oz chicken breast"
            ],
            "instructions": [
                "Marinate the chicken breast in a closed container with 1 teaspoon baking soda and 1/4 cup water for 2 hours in the refrigerator.",
                "After 2 hours, rinse off the baking soda.",
                "Use a tenderizer or your hands to pound the chicken breast.",
                "Set up an assembly line: coat the chicken with egg, then flour, and finally panko bread crumbs.",
                "Air fry the coated chicken breast for 16 minutes at 400°F."
            ]
        },
        {
            "name": "Lemon Fried Chicken",
            "ingredients": [
                "1 teaspoon baking soda",
                "1/4 cup water",
                "Chicken",
                "Lemon juice",
                "Salt",
                "Black pepper"
            ],
            "instructions": [
                "In a closed container, marinate the chicken for 2 hours in the refrigerator with 1 teaspoon of baking soda and 1/4 cup water.",
                "After 2 hours, rinse off the baking soda and marinade the chicken for 1 hour with the spice mix (lemon juice, salt, black pepper).",
                "Wings/Drumsticks: Air fry for 24 minutes at 400°F. Flip halfway through for extra crispiness.",
                "Chicken Breast: Air fry for 16 minutes at 400°F.",
                "Chicken Cutlets: Air fry for 15 minutes at 400°F."
            ]
        },
        {
            "name": "Yogurt Fried Chicken",
            "ingredients": [
                "1 teaspoon baking soda",
                "1/4 cup water",
                "Chicken",
                "Greek Yogurt",
                "Olive Oil",
                "Lemon juice",
                "Ginger",
                "Cumin",
                "Paprika",
                "Oregano",
                "Red chili flakes",
                "Cinnamon",
                "Salt",
                "Pepper",
                "Onion powder"
            ],
            "instructions": [
                "In a closed container, marinate the chicken for 2 hours in the refrigerator with 1 teaspoon of baking soda and 1/4 cup water.",
                "After 2 hours, rinse off the baking soda and marinade the chicken for 1 hour with the spice mix (Greek Yogurt, Olive Oil, Lemon juice, Ginger, Cumin, Paprika, Oregano, Red chili flakes, Cinnamon, Salt, Pepper, Onion powder).",
                "Wings/Drumsticks: Air fry for 24 minutes at 400°F. Flip halfway through for extra crispiness.",
                "Chicken Breast: Air fry for 16 minutes at 400°F.",
                "Chicken Cutlets: Air fry for 15 minutes at 400°F."
            ]
        },
        {
            "name": "Gochujang Fried Chicken",
            "ingredients": [
                "1 teaspoon baking soda",
                "1/4 cup water",
                "Chicken",
                "Gochujang",
                "Soy sauce",
                "Rice wine vinegar",
                "Maple syrup",
                "Garlic",
                "Oil",
                "Gochugaru"
            ],
            "instructions": [
                "In a closed container, marinate the chicken for 2 hours in the refrigerator with 1 teaspoon of baking soda and 1/4 cup water.",
                "After 2 hours, rinse off the baking soda and marinade the chicken for 1 hour with the spice mix (Gochujang, Soy sauce, Rice wine vinegar, Maple syrup, Garlic, Oil, Gochugaru).",
                "Wings/Drumsticks: Air fry for 24 minutes at 400°F. Flip halfway through for extra crispiness.",
                "Chicken Breast: Air fry for 16 minutes at 400°F.",
                "Chicken Cutlets: Air fry for 15 minutes at 400°F."
            ]
        },
        {
            "name": "Serrano Lime Chicken",
            "ingredients": [
                "1 teaspoon baking soda",
                "1/4 cup water",
                "Chicken",
                "Lime juice",
                "Oil",
                "Cumin",
                "Oregano",
                "Garlic",
                "Onion powder",
                "Serrano"
            ],
            "instructions": [
                "In a closed container, marinate the chicken for 2 hours in the refrigerator with 1 teaspoon of baking soda and 1/4 cup water.",
                "After 2 hours, rinse off the baking soda and marinade the chicken for 1 hour with the spice mix (Lime juice, Oil, Cumin, Oregano, Garlic, Onion powder, Serrano).",
                "Wings/Drumsticks: Air fry for 24 minutes at 400°F. Flip halfway through for extra crispiness.",
                "Chicken Breast: Air fry for 16 minutes at 400°F.",
                "Chicken Cutlets: Air fry for 15 minutes at 400°F."
            ]
        },
        {
            "name": "Scotch Bonnet Chicken",
            "ingredients": [
                "1 teaspoon baking soda",
                "1/4 cup water",
                "Chicken",
                "Ginger",
                "Nutmeg",
                "Lime Juice",
                "Garlic",
                "Cinnamon",
                "Black pepper",
                "Scotch Bonett",
                "Allspice",
                "Soy sauce",
                "Scallions",
                "Maple syrup",
                "Thyme leaves",
                "Onion",
                "Water",
                "Salt"
            ],
            "instructions": [
                "In a closed container, marinate the chicken for 2 hours in the refrigerator with 1 teaspoon of baking soda and 1/4 cup water.",
                "After 2 hours, rinse off the baking soda and marinade the chicken for 1 hour with the spice mix (Ginger, Nutmeg, Lime Juice, Garlic, Cinnamon, Black pepper, Scotch Bonett, Allspice, Soy sauce, Scallions, Maple syrup, Thyme leaves, Onion, Water, Salt).",
                "Wings/Drumsticks: Air fry for 24 minutes at 400°F. Flip halfway through for extra crispiness.",
                "Chicken Breast: Air fry for 16 minutes at 400°F.",
                "Chicken Cutlets: Air fry for 15 minutes at 400°F."
            ]
        }
    ],
    "Soup": [
        {
            "name": "Base Soup Recipe",
            "ingredients": [
                "1 tablespoon soup soy sauce",
                "1/2 tablespoon fish sauce",
                "1 tablespoon cooking wine",
                "1 stalk scallion",
                "1 teaspoon salt",
                "1 teaspoon oil",
                "1 teaspoon sesame oil",
                "1 teaspoon white pepper",
                "1 teaspoon brown sugar"
            ],
            "instructions": [
                "Blanch the scallions in oil, then add water.",
                "Add the dashi, fish sauce, cooking wine, salt, white pepper, and brown sugar.",
                "Add any toppings you like.",
                "Once plated, drizzle with sesame oil."
            ]
        },
        {
            "name": "Herbal Beef Bone Soup",
            "ingredients": [
                "2 tablespoons soup soy sauce",
                "1 tablespoon fish sauce",
                "2 tablespoons cooking wine",
                "5 stalks scallions",
                "1 teaspoon salt",
                "1 teaspoon sesame oil",
                "1 teaspoon white pepper",
                "3 lbs beef bones",
                "Mixture of selected herbs",
                "1 yellow onion",
                "5 slices ginger",
                "28 garlic cloves",
                "1 teaspoon brown sugar"
            ],
            "instructions": [
                "Place the beef bones, herbs, scallions, ginger, onion, and garlic in a soup bag at the bottom of a large pot.",
                "Add the dashi, fish sauce, cooking wine, salt, white pepper, and brown sugar to the pot. Cook for 8 hours.",
                "Allow the soup to cool, then refrigerate with the herbs overnight.",
                "The next day, remove the soup bag, reheat the soup, and serve.",
                "Add any toppings you prefer.",
                "Once plated, drizzle with sesame oil."
            ]
        },
        {
            "name": "Herbal Duck Soup",
            "ingredients": [
                "2 tablespoons soup soy sauce",
                "1 tablespoon fish sauce",
                "2 tablespoons cooking wine",
                "5 stalks scallions",
                "1 teaspoon salt",
                "1 teaspoon sesame oil",
                "1 teaspoon white pepper",
                "1 whole duck’s bones",
                "Mixture of selected herbs",
                "1 yellow onion",
                "5 slices ginger",
                "28 garlic cloves",
                "1 teaspoon brown sugar"
            ],
            "instructions": [
                "Place the duck bones, herbs, scallions, ginger, onion, and garlic in a soup bag at the bottom of a large pot.",
                "Add the dashi, fish sauce, cooking wine, salt, white pepper, and brown sugar to the pot. Cook for 8 hours.",
                "Allow the soup to cool, then refrigerate with the herbs overnight.",
                "The next day, remove the soup bag, reheat the soup, and serve.",
                "Add any toppings you prefer.",
                "Once plated, drizzle with sesame oil."
            ]
        },
        {
            "name": "Chicken Noodle Soup",
            "ingredients": [
                "2 tablespoons soup soy sauce",
                "1 tablespoon fish sauce",
                "2 tablespoons cooking wine",
                "5 stalks scallions",
                "1 teaspoon salt",
                "1 teaspoon white pepper",
                "1 whole chicken",
                "Celery",
                "Carrots",
                "1 yellow onion",
                "5 slices ginger",
                "28 garlic cloves",
                "1 teaspoon brown sugar",
                "Noodles"
            ],
            "instructions": [
                "Place the chicken, celery, and carrots in a large pot.",
                "Put the scallions, ginger, onion, and garlic in a soup bag and add it to the pot.",
                "Add the soup soy sauce, fish sauce, cooking wine, salt, white pepper, and brown sugar to the pot. Cook for 3 hours.",
                "About 30 minutes before the soup is finished, cook the noodles in a separate pot.",
                "Remove the soup bag and add the cooked noodles to the chicken soup.",
                "Continue cooking for the remaining 30 minutes, then serve."
            ]
        },
        {
            "name": "Radish Beef Bone Soup",
            "ingredients": [
                "2 tablespoons soup soy sauce",
                "1 tablespoon fish sauce",
                "2 tablespoons cooking wine",
                "5 stalks scallions",
                "1 teaspoon salt",
                "1 teaspoon sesame oil",
                "1 teaspoon white pepper",
                "3 lbs beef short ribs",
                "1 Asian radish",
                "1 yellow onion",
                "5 slices ginger",
                "28 garlic cloves",
                "Sweet potato noodles",
                "Rice",
                "1 teaspoon brown sugar"
            ],
            "instructions": [
                "Soak the beef short ribs in ice water for 30 minutes.",
                "Blanch the beef short ribs in boiling water, then rinse them. Add the ribs to the bottom of a large pot.",
                "Place the scallions, ginger, onion, and garlic in a soup bag and add it to the pot.",
                "Add the soup soy sauce, fish sauce, cooking wine, salt, white pepper, and brown sugar to the pot. Cook on high, uncovered, for 30 minutes.",
                "Remove the radish and cover the pot. Reduce the heat and cook on low for 2 hours.",
                "Prepare the rice and sweet potato noodles.",
                "Slice the radish into small pieces.",
                "Turn off the heat and let the soup rest for 30 minutes.",
                "Remove the soup bags.",
                "Reheat the pot with the radish slices and sweet potato noodles until boiling, then turn off the heat.",
                "For plating, prepare each bowl with a drop of sesame oil, some scallions, a pinch of salt, and black pepper.",
                "Pour the soup into each bowl and serve with rice on the side."
            ]
        },
        {
            "name": "Herbal Chicken Soup",
            "ingredients": [
                "2 tablespoons soup soy sauce",
                "1 tablespoon fish sauce",
                "2 tablespoons cooking wine",
                "5 stalks scallions",
                "1 teaspoon salt",
                "1 teaspoon sesame oil",
                "1 teaspoon white pepper",
                "1 whole chicken",
                "Mixture of selected herbs",
                "1 yellow onion",
                "5 slices ginger",
                "28 garlic cloves",
                "1 teaspoon brown sugar"
            ],
            "instructions": [
                "Place the chicken, herbs, scallions, ginger, onion, and garlic in a soup bag at the bottom of a large pot.",
                "Add the dashi, fish sauce, cooking wine, salt, white pepper, and brown sugar to the pot. Cook for 8 hours.",
                "Allow the soup to cool, then refrigerate with the herbs overnight.",
                "The next day, remove the soup bag, reheat the soup, and serve.",
                "Add any toppings you prefer.",
                "Once plated, drizzle with sesame oil."
            ]
        },
        {
            "name": "Pork and Fuzzy Melon Soup",
            "ingredients": [
                "2 tablespoons soup soy sauce",
                "1 tablespoon fish sauce",
                "2 tablespoons cooking wine",
                "5 stalks scallions",
                "1 teaspoon salt",
                "1 teaspoon sesame oil",
                "1 teaspoon white pepper",
                "500 g pork",
                "Mixture of selected herbs",
                "1 yellow onion",
                "5 slices ginger",
                "28 garlic cloves",
                "1 teaspoon brown sugar"
            ],
            "instructions": [
                "Cut the pork and fuzzy melon into bite-sized pieces.",
                "Blanch the scallion greens in oil, then add water.",
                "Place the herbs, scallion whites, ginger, onion, garlic, and brown sugar in a soup bag at the bottom of a large pot.",
                "Add the dashi, fish sauce, cooking wine, salt, white pepper, pork, and fuzzy melon to the pot. Cook for 2 hours.",
                "Remove the soup bag, then plate the soup.",
                "Once plated, drizzle with sesame oil."
            ]
        },
        {
            "name": "Pork and Thousand Year Egg Congee",
            "ingredients": [
                "Herbal soup (chicken, beef, or duck)",
                "Rice",
                "Dried shiitake mushrooms",
                "500g pork",
                "1 teaspoon baking soda",
                "1/4 cup water",
                "1 teaspoon vegetable oil",
                "1 teaspoon cooking wine",
                "2 teaspoons cornstarch",
                "2 thousand-year eggs",
                "1 stalk scallions",
                "1 teaspoon sesame oil"
            ],
            "instructions": [
                "Marinate the pork in 1 teaspoon baking soda and 1/4 cup water for 2 hours.",
                "Rinse the pork, then marinate it in vegetable oil, cooking wine, and cornstarch for 1 hour.",
                "Soak the shiitake mushrooms in warm water for 1 hour, then slice them into small pieces.",
                "In a pot or rice cooker, combine the rice, marinated pork, shiitake mushrooms, thousand-year eggs, and pre-made herbal soup. If using a pot, remember to soak the rice overnight. Cook until the porridge is ready.",
                "Plate the porridge and garnish with scallion greens and a drizzle of sesame oil."
            ]
        }
    ]
}

# --- Database Functionality ---

DATABASE_FILE = 'recipes.db'

def init_db(db_file):
    """Initializes the SQLite database: creates tables if they don't exist."""
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create Recipes table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            category TEXT NOT NULL
        );
    ''')

    # Create Ingredients table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ingredients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recipe_id INTEGER NOT NULL,
            ingredient_text TEXT NOT NULL,
            FOREIGN KEY (recipe_id) REFERENCES recipes(id) ON DELETE CASCADE
        );
    ''')

    # Create Instructions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS instructions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recipe_id INTEGER NOT NULL,
            step_order INTEGER NOT NULL,
            instruction_text TEXT NOT NULL,
            FOREIGN KEY (recipe_id) REFERENCES recipes(id) ON DELETE CASCADE
        );
    ''')

    # --- NEW: Create Reviews table ---
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recipe_id INTEGER NOT NULL,
            reviewer_name TEXT NOT NULL,
            rating INTEGER NOT NULL, /* 1-5 stars */
            comment TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (recipe_id) REFERENCES recipes(id) ON DELETE CASCADE
        );
    ''')

    conn.commit()
    conn.close()
    print(f"Database schema initialized in '{db_file}'.")

def populate_db(db_file, recipes_data):
    """Populates the database with recipe data."""
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Clear existing data to prevent duplicates if run multiple times
    # (Use with caution in a real application, consider an 'upsert' strategy)
    cursor.execute("DELETE FROM ingredients;")
    cursor.execute("DELETE FROM instructions;")
    cursor.execute("DELETE FROM recipes;")
    # --- NEW: Clear reviews too if repopulating everything ---
    cursor.execute("DELETE FROM reviews;")
    conn.commit()
    print("Cleared existing data from tables.")

    for category, category_recipes in recipes_data.items():
        for recipe in category_recipes:
            recipe_name = recipe['name']
            ingredients = recipe['ingredients']
            instructions = recipe['instructions']

            try:
                cursor.execute(
                    "INSERT INTO recipes (name, category) VALUES (?, ?)",
                    (recipe_name, category)
                )
                recipe_id = cursor.lastrowid
            except sqlite3.IntegrityError:
                print(f"Warning: Recipe '{recipe_name}' already exists. Skipping insertion.")
                # If recipe already exists, we need its ID to link ingredients/instructions
                existing_recipe = cursor.execute("SELECT id FROM recipes WHERE name = ?", (recipe_name,)).fetchone()
                if existing_recipe:
                    recipe_id = existing_recipe[0]
                else:
                    continue # Really shouldn't happen if UNIQUE is working, but safety net

            # Insert ingredients
            for ingredient_text in ingredients:
                cursor.execute(
                    "INSERT INTO ingredients (recipe_id, ingredient_text) VALUES (?, ?)",
                    (recipe_id, ingredient_text)
                )

            # Insert instructions
            for i, instruction_text in enumerate(instructions):
                cursor.execute(
                    "INSERT INTO instructions (recipe_id, step_order, instruction_text) VALUES (?, ?, ?)",
                    (recipe_id, i + 1, instruction_text)
                )
    
    conn.commit()
    conn.close()
    print(f"Database '{db_file}' populated with recipe data.")

def get_all_recipes_from_db(db_file):
    """Fetches all recipes from the database and returns them in a structured dict."""
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    fetched_recipes = {}

    cursor.execute("SELECT id, name, category FROM recipes ORDER BY category, name;")
    db_recipes = cursor.fetchall()

    for db_recipe in db_recipes:
        recipe_id = db_recipe['id']
        recipe_category = db_recipe['category']
        recipe_name = db_recipe['name']

        cursor.execute("SELECT ingredient_text FROM ingredients WHERE recipe_id = ?;", (recipe_id,))
        ingredients = [row['ingredient_text'] for row in cursor.fetchall()]

        cursor.execute("SELECT instruction_text FROM instructions WHERE recipe_id = ? ORDER BY step_order;", (recipe_id,))
        instructions = [row['instruction_text'] for row in cursor.fetchall()]

        if recipe_category not in fetched_recipes:
            fetched_recipes[recipe_category] = []
        
        fetched_recipes[recipe_category].append({
            "name": recipe_name,
            "ingredients": ingredients,
            "instructions": instructions
        })
    
    conn.close()
    return fetched_recipes


# --- Main Execution ---
if __name__ == "__main__":
    # YOU MUST RUN THIS SCRIPT ONCE AFTER MODIFYING IT
    # TO CREATE THE NEW 'REVIEWS' TABLE!
    init_db(DATABASE_FILE)
    populate_db(DATABASE_FILE, recipes) # This will also clear existing reviews for a fresh start

    print("\n--- Verifying data by reading from DB (includes reviews table now) ---")
    retrieved_recipes = get_all_recipes_from_db(DATABASE_FILE)
    # print(json.dumps(retrieved_recipes, indent=2)) # Uncomment to see recipe data
    print("\nDatabase operations complete. Check your directory for 'recipes.db'.")

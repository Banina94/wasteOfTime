from flask import Flask, render_template, g, request, redirect, url_for
import sqlite3
import datetime # For formatting timestamps

app = Flask(__name__)
DATABASE = 'recipes.db'

# --- Database Helper Functions (Keep as is) ---
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

# --- Category Descriptions (Keep as is) ---
category_descriptions = {
    # ... (your existing category_descriptions here) ...
    "Cookies": """
        <p>This page contains eight cookie recipes based on the
        same basic formula. From this starting point, you can continue to build and
        customize your own recipes. I hope this book serves as a foundation for your
        experimentation and exploration in creating your own unique cookies.</p>

        <p>In my recipes, I recommend freezing the cookie dough for
        several reasons. The first is for portion control and health benefits. Freezing
        the dough allows you to bake one cookie at a time whenever you crave one,
        rather than eating a dozen at once. This helps satisfy cravings while keeping
        portions in check. The second reason is that it creates a unique texture for
        the cookies. Freezing helps the crust become crispier, while the inside stays
        soft and chewy. The final reason I recommend freezing the dough is that it
        simplifies the baking process. The baking time and temperature remain
        consistent for all recipes, as long as the freezer temperature is controlled
        and the cookies are baked directly from the freezer (not allowed to reach room
        temperature).</p>

        <p>Here are a few additional tips and tricks for baking
        cookies:</p>
        <ul>
            <li>I recommend always sifting or weighing the flour. If you use measuring cups and don’t sift the flour, the cookies will end up too dense. Aerating the flour before measuring is key to getting the right texture.</li>
            <li>I alternate between ghee and butter depending on the melting point. For tea-infused cookies, I prefer using ghee, since it is a liquid at room temperature, which helps the tea flavor infuse better. For all other cookies, I use butter, which is solid at room temperature and adds a rich flavor. Ghee has a distinct taste that some people may not like. If you prefer not to use ghee, I recommend using a neutral-flavored oil that is also liquid at room temperature. When using ghee or oil, the cookie dough must be frozen before baking or else the cookie will spread upon contact with heat.</li>
        </ul>
    """,
    "Fried Chicken": """
        <p>Fried chicken is a classic dish beloved by many. Like
        any other dish in cooking, once the base concepts are mastered, you can explore
        and experiment as you wish. While there are countless ways to prepare it, at
        its core, making fried chicken requires tenderizing the meat. Whether through
        acid, spice, chemicals, or physical techniques, something must break down the
        fibers to achieve a tender and juicy result. In this book, I’ve included eight
        different methods for making fried chicken, each using a variety of approaches
        based on the same fundamental concept. Feel free to explore these recipes and
        adapt them to suit your own tastes.</p>

        <p>I like to begin all my chicken recipes by soaking the
        chicken in a mixture of baking soda and water. No matter what you do
        afterwards, this step helps ensure the chicken turns out juicy and flavorful.
        Just be sure to rinse off the baking soda thoroughly to avoid any unpleasant
        aftertaste.</p>

        <p>Let me know about all the different spices you experiment
        with! Buttermilk coating and buffalo sauce are just a couple of the options not
        covered in this book. Here are a few tips for preparing these dishes:</p>
        <ul>
            <li>The longer you marinate the chicken with the spice mix, the more flavor will be absorbed into the meat.</li>
            <li>Be cautious about salmonella. Make sure the chicken is fully cooked. Since air fryers vary in performance, adjust the cooking time and temperature based on your specific model. Also, ensure the chicken is fully covered while marinating and always store it in the refrigerator defrosted for less than three days.</li>
        </ul>
    """,
    "Soup": """
        <p>Similar to the page on Eight Cookie Recipes, this page
        features eight soup recipes, all built from a simple base recipe. While brand
        choices aren’t crucial, each soup recipe includes fish sauce, soup soy sauce,
        and cooking wine. I typically use Thai fish sauce, Korean soup soy sauce, and
        Chinese cooking wine. Korean soup soy sauce is made from water, soybeans, salt,
        and spirits. The Thai fish sauce consists of anchovy extract, water, salt, and
        sugar. Lastly, the Chinese cooking wine is the classic Shao Xing cooking wine
        used in most Chinese dishes, made from water, rice, wheat, salt, and caramel.</p>

        <p>I like to use the herbal soup as a base for many other
        dishes because it adds the added benefit of the herbs’ nutrients. Once the
        herbal soup is made, it works wonderfully as a base for flavored rice. Try
        substituting the herbal soup for water when cooking rice to enhance the dish’s
        flavor—similar to Hainanese chicken rice. The herbal soup base can also be
        frozen and used for hot pot instead of store-bought broth. Additionally, in
        dizhes like egg soufflé, gyudon, and others, the soup base can replace water to
        enrich the flavor. In this book, the last recipe of pork and thousand year egg
        porridge is an example of how the herbal soup can be applied as a base for
        other dishes.</p>

        <p>Feel free to adjust the base recipe as you like, but here
        are some common tips and tricks I often use:</p>
        <ol>
            <li>The exact ratio of soy sauce, fish sauce, and cooking wine isn’t crucial, nor is the quantity of any of the ingredients. Feel free to experiment with the amounts until you find a flavor profile you like. Just be mindful that some herbs should be consumed in moderation.</li>
            <li>There is a wide variety of herbs to include, especially Chinese herbs. Since our typical diet is rich in oil, flavor, and energy, we favor cooling herbs like dried Ziziphus jujuba (dried dates), dried fox nuts, dried pearl barley, and Poria cocos.</li>
        </ol>
    """
}

# --- Routes ---

@app.route('/')
def index():
    categories = query_db('SELECT DISTINCT category FROM recipes ORDER BY category;')
    return render_template('index.html', categories=categories)

@app.route('/category/<category_name>')
def show_category(category_name):
    recipes_in_category = query_db(
        'SELECT id, name FROM recipes WHERE category = ? ORDER BY name;',
        (category_name,)
    )
    blurb = category_descriptions.get(category_name, "")
    return render_template('category.html',
                           category=category_name,
                           recipes=recipes_in_category,
                           blurb=blurb)

@app.route('/recipe/<int:recipe_id>')
def show_recipe(recipe_id):
    recipe = query_db('SELECT id, name, category FROM recipes WHERE id = ?;', (recipe_id,), one=True)
    if recipe is None:
        return "Recipe not found!", 404

    ingredients = query_db('SELECT ingredient_text FROM ingredients WHERE recipe_id = ? ORDER BY id;', (recipe_id,))
    instructions = query_db('SELECT instruction_text FROM instructions WHERE recipe_id = ? ORDER BY step_order;', (recipe_id,))

    # --- NEW: Fetch reviews for this recipe ---
    reviews = query_db('SELECT reviewer_name, rating, comment, created_at FROM reviews WHERE recipe_id = ? ORDER BY created_at DESC;', (recipe_id,))

    # --- NEW: Calculate average rating ---
    average_rating = 0
    num_reviews = len(reviews)
    if num_reviews > 0:
        total_rating = sum(review['rating'] for review in reviews)
        average_rating = round(total_rating / num_reviews, 1) # Round to one decimal place

    return render_template('recipe.html',
                           recipe=recipe,
                           ingredients=ingredients,
                           instructions=instructions,
                           reviews=reviews, # Pass reviews to template
                           average_rating=average_rating, # Pass average rating
                           num_reviews=num_reviews) # Pass number of reviews

# --- NEW: Route for submitting reviews ---
@app.route('/submit_review', methods=['POST'])
def submit_review():
    recipe_id = request.form.get('recipe_id')
    reviewer_name = request.form.get('reviewer_name')
    rating = request.form.get('rating')
    comment = request.form.get('comment')

    # Basic validation
    if not recipe_id or not reviewer_name or not rating:
        # In a real app, you'd use flash messages for user feedback
        print("Error: Missing recipe_id, reviewer_name, or rating.")
        return redirect(url_for('show_recipe', recipe_id=recipe_id))

    try:
        recipe_id = int(recipe_id)
        rating = int(rating)
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
    except (ValueError, TypeError):
        print("Error: Invalid recipe_id or rating.")
        return redirect(url_for('show_recipe', recipe_id=recipe_id))

    # Optional: Basic sanitation for comment/name (though not full security)
    reviewer_name = reviewer_name.strip()
    comment = comment.strip()

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO reviews (recipe_id, reviewer_name, rating, comment) VALUES (?, ?, ?, ?)",
        (recipe_id, reviewer_name, rating, comment)
    )
    conn.commit()
    
    print(f"Review submitted for recipe_id {recipe_id} by {reviewer_name} with {rating} stars.")
    return redirect(url_for('show_recipe', recipe_id=recipe_id))


if __name__ == '__main__':
    app.run(debug=True)
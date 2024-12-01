from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load recipes from JSON file
with open('recipes.json', 'r') as file:
    recipes = json.load(file)

@app.route('/')
def index():
    return render_template('index.html', recipes=recipes)

@app.route('/recipe/<int:recipe_id>')
def recipe(recipe_id):
    recipe = next((r for r in recipes if r['id'] == recipe_id), None)
    if recipe:
        return render_template('recipe.html', recipe=recipe)
    else:
        return "Recipe not found", 404

if __name__ == '__main__':
    app.run(debug=True)

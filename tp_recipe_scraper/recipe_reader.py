class Recipe:
    def __init__(self, title, ingredients, instructions, nutrients):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.nutrients = nutrients

    def __str__(self):
        return self.title


import json
import re

file_path = r"C:\Users\mleyoncour2024\Documents\python\tp_recipe_scraper\demofile.txt"

with open(file_path, "r", encoding="utf-8") as file:
    raw_content = file.read().strip()

if not raw_content.startswith("["):
    raw_content = f"[{raw_content}]"

raw_content = re.sub(r",\s*\]", "]", raw_content)


try:
    data_list = json.loads(raw_content)
except json.JSONDecodeError as e:
    print("Erreur de parsing JSON :", e)
    data_list = []

class Recipe:
    def __init__(self, title, ingredients, instructions, nutrients):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.nutrients = nutrients

    def __str__(self):
        return self.title

recipes = []
for data in data_list:
    recipe = Recipe(
        title=data.get("title", "Sans titre"),
        ingredients=data.get("ingredients", []),
        instructions=data.get("instructions", ""),
        nutrients=data.get("nutrients", {})
    )
    recipes.append(recipe)

for r in recipes:
    print(r)

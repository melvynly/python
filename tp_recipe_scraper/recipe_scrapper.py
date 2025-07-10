# utilise le code suivant pour stocker dans un fichier json
# les informations title, instructions, ingredients et nutrients
# de chaque recette de cuisine présente dans la liste des urls
# PS recipe_scrapers vient de https://github.com/hhursev/recipe-scrapers

# crée ensuite un script de lecture du fichier
# et une classe Recipe
# qui représente une recette extraite d'une url

# PS : commence ton TP avec une ou deux urls pour ensuite faire le processus sur les 100 urls présentes

from recipe_scrapers import scrape_me
import json

urls = ['https://www.allrecipes.com/recipe/21014/good-old-fashioned-pancakes/'
    , 'https://www.allrecipes.com/recipe/22162/uglies/', 'https://www.allrecipes.com/recipe/140286/homemade-dog-food/',
        'https://www.allrecipes.com/the-10-minute-recipe-i-make-once-a-week-11742451']


for i, url in enumerate(urls):
    try:
        scraper = scrape_me(url)
        titre = scraper.title()
        instructions = scraper.instructions()
        ingredients = scraper.ingredients()
        nutrients = scraper.nutrients()

        recipe_data = {
            "title": scraper.title(),
            "instructions": scraper.instructions(),
            "ingredients": scraper.ingredients(),
            "nutrients": scraper.nutrients() if hasattr(scraper, 'nutrients') else None
        }
        recipe_json = json.dumps(recipe_data, indent=4, ensure_ascii=False)
        print(recipe_json)

        with open("demofile.txt", "a") as f:
            f.write(f"{recipe_json},")
            f.write("\n")

    #json.dumps
    except Exception as e:
        print(f"❌  Erreur sur {url} : {e}")

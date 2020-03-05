from bs4 import BeautifulSoup

import requests


class RecipeFetcher:

    def search_recipes(self, url):
        search_url = url

        page_html = requests.get(search_url)
        page_graph = BeautifulSoup(page_html.content, features="lxml")

        return [recipe.a['href'] for recipe in \
                page_graph.find_all('div', {'class': 'grid-card-image-container'})]

    def scrape_recipe(self, recipe_url):
        results = {}

        page_html = requests.get(recipe_url)
        page_graph = BeautifulSoup(page_html.content, features="lxml")
        results['ingredients'] = [ingredient.text for ingredient in \
                                  page_graph.find_all('span', {'itemprop': 'recipeIngredient'})]

        results['labels'] = [ingredient.text for ingredient in \
                             # page_graph.find_all('span', {'itemprop':'recipeIngredient'})
                             page_graph.find_all('span', {'data-id': '0'})]

        results['directions'] = [direction.text.strip() for direction in \
                                 page_graph.find_all('span', {'class': 'recipe-directions__list--item'})
                                 if direction.text.strip()]
        for i in results['ingredients']:
            if i in results['labels']:
                results['ingredients'].remove(i)

        return results


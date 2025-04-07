import requests
from parsel import Selector

from scrapping.bbc_food.models.recipe import Recipe
from scrapping.helpers import catch


class CollectRecipes:

    def start_collection(self, search_term):
        result = requests.get(f"https://www.bbcgoodfood.com/search?q={search_term}")
        html = Selector(result.text)
        recipe_nodes = html.xpath("//div[@class='search-result--list']").getall()

        results = []
        for node in recipe_nodes:
            recipe = self.create_recipe(node)
            results.append(recipe)

        return results


    @catch
    def create_recipe(self, html):
        card_sections_1 = Selector(html).xpath(".//div[@class='card__section card__content']")
        card_sections_2 = Selector(html).xpath(".//div[@class='card__section card__footer']")
        return Recipe(
            title = card_sections_1.xpath(".//h2/text()").get(),
            description = card_sections_1.xpath(".//p/text()").get(),
            time = card_sections_2.xpath(".//ul/li[1]/span/text()").get(),
            difficulty = card_sections_2.xpath(".//ul/li[2]/span/text()").get(),
            vegan = card_sections_2.xpath(".//ul/li[3]/span/text()").get() is not None,
            gluten_free = card_sections_2.xpath(".//ul/li[4]/span/text()").get() is not None
        )
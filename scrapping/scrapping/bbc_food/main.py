from scrapping.bbc_food.collect_recipes import CollectRecipes


def default(args):
    search_terms = args[0]

    results = []
    for i in CollectRecipes().start_collection(search_terms):
        data = {
            "title": i.title,
            "description": i.description,
            "time": i.time,
            "difficulty": i.difficulty,
            "vegan": i.vegan,
            "gluten_free": i.gluten_free,
        }
        results.append(data)
    return results

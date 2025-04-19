from scrapping.bbc_food.collect_recipes import CollectRecipes
from scrapping.run import Runner


def default(args, **kwargs):
    runner: Runner = kwargs['runner']
    search_terms = args[0]

    collector = CollectRecipes()
    runner.submit_work(collector.start_collection, search_term)

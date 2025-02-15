import importlib
import sys


def run_scrpaer(scraper, args):
    try:
        scraper = importlib.import_module(f'scrapping.{scraper}.main')
        entry_point = getattr(scraper, 'default')
        return entry_point(args)
    except ModuleNotFoundError as e:
        print(f'scraper {scraper} not found {e}')
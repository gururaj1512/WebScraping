import importlib
import sys
from scrapping.output import dump_to_file


def default():
    module = sys.argv[1]
    try:
        scraper = importlib.import_module(f'scrapping.{module}.main')
        entry_point = getattr(scraper, 'default')
        results = entry_point(sys.argv[2:])
        dump_to_file(results)
    except ModuleNotFoundError:
        print(f'module {module} not found')
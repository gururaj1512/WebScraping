import sys
from scrapping import run, output


def default():
    module = sys.argv[1]
    results = run.run_scrpaer(module, sys.argv[2:])
    output.dump_to_file(results)

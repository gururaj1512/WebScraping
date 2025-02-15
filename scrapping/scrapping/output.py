import json


def dump_to_file(results):
    with open('./output.json', 'w') as f:
        json.dump(results, f)
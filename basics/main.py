from requests import get
import json
import sys
from xpath_scraper import get_opponents, get_fighter_info


if len(sys.argv) == 1:
    raise Exception('missing argument...!')
target = sys.argv[1]
output = sys.argv[2]
url = sys.argv[3]

handler = None
if target == 'ops':
    handler = get_opponents
elif target == 'info':
    handler = get_fighter_info

response = get(url)
result = handler(response.text)
json_format = json.dumps(result)

with open(f'{output}.json', 'w') as f:
    f.write(json_format)



# info_json = json.dumps(info)

# with open('khabib_info.json', 'w') as f:
#     f.write(info_json)

# opponents = get_opponents(response.text)

# opponents_json = json.dumps(opponents)

# with open('khabib_opponents.json', 'w') as f:
#     f.write(opponents_json)

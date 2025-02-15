import requests
from bs4 import BeautifulSoup

response = requests.get("https://en.wikipedia.org/wiki/Lionel_Messi")
# print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

tables = soup.find_all("table", attrs={"class": "wikitable"})
matches = tables[1]
trs = matches.find_all("tr")

goals = []
for tr in trs:
    td = tr.find_all("td")
    if not td:
        continue

    year_node = td[0].string
    goal_node = td[-1].string
    if not year_node:
        continue
    goals.append((year_node.replace("\n", ""), goal_node.replace("\n", "")))

print(goals)


# with open("messi.html", "w", encoding="utf-8") as f:
#     f.write(response.text)
# print(soup.title)
# tables = soup.find_all("table")
# print(tables)
# table = soup.find_all("table", attrs={"class": "wikitable"})
# print(table)
import requests
from bs4 import BeautifulSoup

url = "https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")
table = soup.find('tbody')

rows = table.find_all('tr')
stats = []

for row in rows:
	cols = row.find_all('td')
	d = {}
	for col in cols:
		datastat = col["data-stat"]
		txt = col.text
		d[datastat] = txt
	stats.append(d)


team = input("Vilket lag vill du se? ")
for statdict in stats:
	if (statdict["score"] != ""):
		if (statdict["home_team"] == team):
			print(statdict["date"], statdict["home_team"], statdict["home_xg"], statdict["score"])

print("--")
for statdict in stats:
	if (statdict["score"] != ""):
		if (statdict["away_team"] == team):
			print(statdict["date"], statdict["away_team"], statdict["away_xg"], statdict["score"])




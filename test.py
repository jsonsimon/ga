import requests
from bs4 import BeautifulSoup

url = "https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")
table = soup.find('tbody')

rows = table.find_all('tr')
stats = []
count = 0
for row in rows:
	cols = row.find_all('td')
	d = {}
	for col in cols:
		datastat = col["data-stat"]
		txt = col.text
		d[datastat] = txt
	stats.append(d)
	count = count+1
#print(stats)

for statdict in stats:
	if (statdict["score"] != ""):
		print(statdict["home_team"], statdict["home_xg"], statdict["score"], statdict["away_xg"], statdict["away_team"])

#table=table.replace("Match Report", "\n")
#table=table.replace("Head-to-Head", "\n")

#print(table)
#print(row[1])



import pandas as pd
import requests
from bs4 import BeautifulSoup

round = 0
while round < 4:
	sesstart = 2024-round
	sesend = sesstart+1
	sesinurl = str(sesstart)+"-"+str(sesend)

	url = "https://fbref.com/en/comps/9/{}/schedule/{}-Premier-League-Scores-and-Fixtures".format(sesinurl, sesinurl)

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
		if d["dayofweek"] != '':
			stats.append(d)

	df = pd.DataFrame(stats)

	df.to_csv('table'+sesinurl+'.csv', index=False)
	round = round+1
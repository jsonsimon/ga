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
	week = []

	for row in rows:
		cols = row.find_all('td')
		d = {}
		for col in cols:
			datastat = col["data-stat"]
			txt = col.text
			d[datastat] = txt
		if d["dayofweek"] != '':
			stats.append(d)
		cols2 = row.find_all('th')
		for col2 in cols2:
			gameweek = col2['data-stat']
			d2 = {}
			txt2 = col2.text
			d2[gameweek] = txt2
		if d2["gameweek"] != '':
			week.append(d2)
	df2 = pd.DataFrame(week)
	
	df = pd.DataFrame(stats)
	df["matchweek"] = df2

	df.to_csv('table'+sesinurl+'.csv', index=False)
	round = round+1
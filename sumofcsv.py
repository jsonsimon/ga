import pandas as pd

sumdf = pd.concat(map(pd.read_csv, ["table2021-2022.csv", "table2022-2023.csv", "table2023-2024.csv", "table2024-2025.csv"]), ignore_index=True)

sumdf = sumdf[sumdf["score"].notna()]
manuloc = sumdf["score"].str.replace("–", "-")
gd  = manuloc.apply(eval)

sumdf["gd"] = gd

test = sumdf["score"]
hg2 = []
ag2 = []

for i in test:
	hg = (i[0])
	ag = (i[2])
	hg2.append(hg)
	ag2.append(ag)

dfh = pd.DataFrame(hg2)
dfa = pd.DataFrame(ag2)

sumdf.reset_index(drop=True, inplace=True)

sumdf["hg"] = dfh
sumdf["ag"] = dfa

teams = []
tdf = sumdf["home_team"]
statdf = []

#making ints and floats of the numbers in sumdf
sumdf = sumdf.astype({'hg':'int'})
sumdf = sumdf.astype({'ag':'int'})
sumdf = sumdf.astype({'home_xg':'float'})
sumdf = sumdf.astype({'away_xg':'float'})
# sumdf = sumdf.astype({'attendance':'int'}) //behöver byta ut "," till "" för att kunna göra floats utav de

for z in tdf:
	if not z in teams:
		teams.append(z)

for team in teams:
	hteam = sumdf[sumdf ["home_team"] == team]
	ateam = sumdf[sumdf["away_team"] == team]

	#creating statisticvariables
	games = len(hteam)+len(ateam)
	wins = (hteam["gd"] > 0).sum() + (ateam["gd"] < 0).sum()
	ties = (hteam["gd"] == 0).sum() + (ateam["gd"] == 0).sum()
	losses = games-wins-ties
	winrate = wins/games
	hgoals = hteam["hg"].sum()
	agoals = ateam["ag"].sum()
	goals = hgoals+agoals
	xg_avg = (hteam["home_xg"].sum() + ateam["away_xg"].sum())/games
	gpg = goals/games
	#attendence_avg = hteam["attendence"]/len(hteam)

	#collecting the variables into a dict to make it a dataframe
	statdict = {
		"team":team,
		"games":games,
		"wins":wins,
		"ties":ties,
		"losses":losses,
		"winrate":winrate,
		"goals":goals,
		"homegoals":hgoals,
		"awaygoals":agoals,
		"goalspergame":gpg,
		"xg_avg":xg_avg
	}
	statdf.append(statdict) 

sdf = pd.DataFrame(statdf)

sumdf.to_csv("sumdftest.csv", index=False)
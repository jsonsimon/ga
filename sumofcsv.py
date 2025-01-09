from datetime import date
import pandas as pd

sumdf = pd.concat(map(pd.read_csv, ["table2021-2022.csv", "table2022-2023.csv", "table2023-2024.csv", "table2024-2025.csv"]), ignore_index=True) #import csvfiles
sumdf2 = pd.concat(map(pd.read_csv, ["table2024-2025.csv"]), ignore_index=True) 

sumdf = sumdf[sumdf["score"].notna()] #removal of games not yet played
noplay = sumdf2[sumdf2["score"].isna()]
sumdf2 = sumdf2[sumdf2["score"].notna()] #removal of games not yet played
manuloc = sumdf["score"].str.replace("–", "-") #html "-"" to math "-" to use eval
gd  = manuloc.apply(eval) 
sumdf["attendance"] = sumdf["attendance"].str.replace(",", "") #removal of "," to make strings into ints
sumdf["attendance"] = sumdf["attendance"].fillna(0) #switching of "NaN" to "0" to make strings into ints
sumdf["date"] = pd.to_datetime(sumdf["date"]) #making date inte pandas date

sumdf["gd"] = gd #add goal difference to dataframe

#collecting goals scored by home team and awayteam and adding to the dataframe (will not work if a team scores more than 10 goals in a match (has never happened in the premier leauge))
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

sumdf.reset_index(drop=True, inplace=True) #fixes bug from wrong indexation because of the removal of postponed games (row 5)

sumdf["hg"] = dfh
sumdf["ag"] = dfa
###

#making ints and floats of the numbers in sumdf
sumdf = sumdf.astype({'hg':'int'})
sumdf = sumdf.astype({'ag':'int'})
sumdf = sumdf.astype({'home_xg':'float'})
sumdf = sumdf.astype({'away_xg':'float'})
sumdf = sumdf.astype({'attendance':'int'})
###

tdf = sumdf["home_team"]
teams = []
statdf = []

#making a list of teams
for z in tdf:
	if not z in teams:
		teams.append(z)
###

#making dataframes only including one team
for team in teams:
	hteam = sumdf[sumdf ["home_team"] == team]
	ateam = sumdf[sumdf["away_team"] == team]
###

	#creating statisticvariables
	games = len(hteam)+len(ateam)
	wins = (hteam["gd"] > 0).sum() + (ateam["gd"] < 0).sum()
	ties = (hteam["gd"] == 0).sum() + (ateam["gd"] == 0).sum()
	losses = games-wins-ties
	winrate = f"{round((wins / games) * 100, 2)}%"
	hgoals = hteam["hg"].sum()
	agoals = ateam["ag"].sum()
	goals = hgoals+agoals
	gpg = goals/games
	xg_avg = (hteam["home_xg"].sum() + ateam["away_xg"].sum())/games
	xg_against_avg = (hteam["away_xg"].sum() + ateam["home_xg"].sum())/games
	conceded = (hteam["ag"].sum() + ateam["hg"].sum())
	concededpergame = conceded/games
	attendence_avg = f"{round(hteam["attendance"].sum()/(len(hteam)-(hteam["attendance"] == 0).sum()), 0)}"
	###

	#collecting the variables into a dict
	statdict = {
		"team":team,
		"games":games,
		"wins":wins,
		"ties":ties,
		"losses":losses,
		"winrate":winrate, 
		"goals":goals,
		"conceded":conceded,
		"homegoals":hgoals,
		"awaygoals":agoals,
		"goalspergame":gpg,
		"xg_avg":xg_avg,
		"xg_against_avg":xg_against_avg,
		"concededpergame":concededpergame,
		"attendance_avg":attendence_avg
	}
	statdf.append(statdict) 
	###

sdf = pd.DataFrame(statdf) #making dataframe of statdict

#sdf.to_csv("sumdftest.csv", index=False)

hxgavg = sumdf["home_xg"].sum()/len(sumdf["home_xg"])
axgavg = sumdf["away_xg"].sum()/len(sumdf["away_xg"])

next_matchweek = sumdf2["matchweek"].max() + 1

filtermatches = noplay[noplay["matchweek"] == next_matchweek]
home = [filtermatches["home_team"]]
away = [filtermatches["away_team"]]
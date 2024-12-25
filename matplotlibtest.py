import matplotlib.pyplot as plt
import pandas as pd

pd.options.mode.copy_on_write = True
#sumdf = pd.concat(map(pd.read_csv, ["table2021-2022.csv", "table2022-2023.csv", "table2023-2024.csv", "table2024-2025.csv"]), ignore_index=True)
sumdf = pd.concat(map(pd.read_csv, ["table2024-2025.csv"]), ignore_index=True)

winner = []
sumdf = sumdf[sumdf["score"].notna()] #removal of games not yet played
manuloc = sumdf["score"].str.replace("–", "-") #html "-"" to math "-" to use eval
gd  = manuloc.apply(eval) 

sumdf["gd"] = gd #add goal difference to dataframe

for index, row in sumdf.iterrows():
    if row['gd'] < 0: 
        winner.append(row['away_team'])
    elif row['gd'] > 0:
        winner.append(row['home_team'])
    else:
        winner.append('tie')
win = pd.DataFrame(winner)

sumdf["winner"] = win
tdf = sumdf["home_team"]
teams = []
winnerdf = []

for z in tdf:
    if not z in teams:
        teams.append(z)

for team in teams:
    hteam = sumdf[sumdf ["home_team"] == team]
    ateam = sumdf[sumdf["away_team"] == team]
    for index, row in hteam.iterrows():
        if row["gd"] > 0:
            winnerdict = {team:int(2),
            'date':row['date'],
                }
        elif row["gd"] < 0:
            winnerdict = {team:int(0),
            'date':row['date'],
            }
            winnerdf.append(winnerdict)
        else:
            winnerdict = {team:int(1),
            'date':row['date'],
            }
            winnerdf.append(winnerdict)
    for index, row in ateam.iterrows():
        if row["gd"] < 0:
            winnerdict = {team:int(2),
            'date':row['date'],
            }
            winnerdf.append(winnerdict)
        elif row["gd"] > 0:
            winnerdict = {team:int(0),
            'date':row['date'],
            }
            winnerdf.append(winnerdict)
        else:
            winnerdict = {team:int(1),
            'date':row['date'],
            }
            winnerdf.append(winnerdict)
hej = pd.DataFrame(winnerdf)
hej.set_index('date')

#hej['date'] = pd.to_datetime(hej['date'])


#hej['date'] = hej['date'].dt.strftime('%Y-%m-%d')
print(hej.to_string())

hej.plot.scatter(x='date', y= 'Manchester Utd')
plt.show()
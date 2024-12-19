import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('bmh')
df = sumdf = pd.concat(map(pd.read_csv, ["table2021-2022.csv", "table2022-2023.csv", "table2023-2024.csv", "table2024-2025.csv"]), ignore_index=True)

winner = []
sumdf = sumdf[sumdf["score"].notna()] #removal of games not yet played
manuloc = sumdf["score"].str.replace("–", "-") #html "-"" to math "-" to use eval
gd  = manuloc.apply(eval) 
sumdf["attendance"] = sumdf["attendance"].str.replace(",", "") #removal of "," to make strings into ints
sumdf["attendance"] = sumdf["attendance"].fillna(0) #switching of "NaN" to "0" to make strings into ints
sumdf["date"] = pd.to_datetime(sumdf["date"]) #making date inte pandas date

sumdf["gd"] = gd #add goal difference to dataframe

for index, row in sumdf.iterrows():
    if row['gd'] < 0: 
        winner.append(row['away_team'])
    elif row['gd'] < 0: 
        winner.append(row['home_team'])
    else:
        winner.append('tie')
win = pd.DataFrame(winner)

sumdf["winner"] = win




'''
# All teams
x = df['date']
y = df['winner']

# Bar chart
plt.xlabel('date', fontsize=18)
plt.ylabel('winner', fontsize=16)
plt.bar(x, y)

plt.show()

# Den blev as skev men testa bara lite
'''
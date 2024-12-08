import pandas as pd

sumdf = pd.concat(map(pd.read_csv, ["table2021-2022.csv", "table2022-2023.csv", "table2023-2024.csv", "table2024-2025.csv"]), ignore_index=True)

manu = sumdf[sumdf["score"].notna()]
manuloc = manu["score"].str.replace("–", "-")
gd  = manuloc.apply(eval)

sumdf["gd"] = gd

test = manu["score"]
hg2 = []
ag2 = []

for i in test:
	hg = (i[0])
	ag = (i[2])
	hg2.append(hg)
	ag2.append(ag)

dfh = pd.DataFrame(hg2)
dfa = pd.DataFrame(ag2)


sumdf["hg"] = dfh
sumdf["ag"] = dfa

arshome = sumdf[sumdf ["home_team"] == "Arsenal"]

arshome.to_csv("arshome.csv", index=False)

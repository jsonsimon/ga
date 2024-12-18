import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('bmh')
df = pd.read_csv('sumdftest.csv')

# All teams
x = df['team']
y = df['winrate']

# Bar chart
plt.xlabel('team', fontsize=4)
plt.ylabel('winrate(%)', fontsize=16)
plt.bar(x, y)

plt.show()

# Den blev as skev men testa bara lite
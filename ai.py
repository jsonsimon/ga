from openai import OpenAI
import pandas as pd
import sumofcsv
import markdown
import webbrowser
import datetime

current_time = datetime.    datetime.now()


formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")



client = OpenAI()

file = sumofcsv.sdf
sumdf = sumofcsv.sumdf
home = sumofcsv.home
away = sumofcsv.away

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a professional sports analyst that analyzes Premier League."},
        {
            "role": "user",
            "content": ("Based on contents in the dataframes:{} and {}, who would most likely win a game between {} and {} where the first team is home and the second is away? Pick teams on the same row, make 10 simulations and give the average, and then go again until all matches are counted for, display the results in a user-friendly UI for html use with game, winner, and score (home team first and away team second). Focus extra on recent results (the last 8 games the team has played) whilst still using facts, statistics and earlier games between the two teams to back your predictions up. Only give me a winner prediction, a likely score, and a short explanation. Make a user-friendly UI for html use with game, winner, and score (home team first and away team second) to display your predictions. Put the explanations later and include the specific numbers used.").format(file, sumdf, home, away)
        }
    ]
)

html = markdown.markdown(completion.choices[0].message.content)

filename = f"predictions_{formatted_time}.html"

with open(filename, "w", encoding="utf-8") as f:
    f.write(html)

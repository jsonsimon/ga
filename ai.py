from openai import OpenAI
import pandas as pd
import sumofcsv

client = OpenAI()

file = sumofcsv.sdf
sumdf = sumofcsv.sumdf
home = sumofcsv.home
away = sumofcsv.away

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a proffesional sports analasyst that analyzes Premier League."},
        {
            "role": "user",
            "content": ("Based on contents in the dataframes:{} and {}, who would most likley win a game between {} and {} where the first team is home and the second is away? Pick teams on the same row make 10 simulations and give the average and then go again until all matches are counted for. Focus extra on recent results whilst still using facts to back your predictions up. Only give me a winner prediction, a likely score and a short explanation in swedish. Make a user friendly UI to display your predictions").format(file, sumdf, home, away)
        }
    ]
)

print(completion.choices[0].message)
from openai import OpenAI
import pandas as pd
import sumofcsv

client = OpenAI()

file = sumofcsv.sdf
sumdf = sumofcsv.sumdf

home = input("Hemmalag: ")
away = input("Bortalag: ")

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a proffesional sports analasyst."},
        {
            "role": "user",
            "content": ("Based on contents in the dataframes:{} and {}, who would most likley win a game between {} and {} where the first team is home and the second is away? Focus extra on the current form of the team. Only give me a winner prediction, a likely score and a short explanation in swedish.").format(file, sumdf, home, away)
        }
    ]
)

print(completion.choices[0].message)
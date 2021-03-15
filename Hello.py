import pandas as pd
import numpy as np

data = {'date': ['02-08-1992', '04-22-1985', '07-03-2001'], 'food': ['scrapple', 'pork roll', 'sausage']}
df = pd.DataFrame(data=data)

def split_dates(date_seris):
    date_seris['date'] = pd.to_datetime(date_seris['date'], infer_datetime_format = True)
    date_seris['year'] = date_seris['date'].dt.year
    date_seris['month'] = date_seris['date'].dt.year
    date_seris['day'] = date_seris['date'].dt.year
    return date_seris

def null_count(df):
    null = df.insull().sum().sum()
    return null

print(split_dates(df))
print(null_count(df))
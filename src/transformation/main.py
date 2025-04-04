import pandas as pd
from datetime import datetime

#Set the path for the JSONL file
df = pd.read_json('../data/data.jsonl', lines=True)

#Add the column _source with a fixed value
df['_source'] = "https://lista.mercadolivre.com.br/tenis-corrida-masculino"

#Add the column _data_coleta with the current date and time
df['_data_coleta'] = datetime.now ()

#Handle null values for numeric and text columns
df['old_price'] = df['old_price'].fillna(0).astype(float)
df['old_price_cents'] = df['old_price_cents'].fillna(0).astype(float)
df['new_price'] = df['new_price'].fillna(0).astype(float)
df['new_price_cents'] = df['new_price_cents'].fillna(0).astype(float)
df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(float)
df['reviews_amount'] = df['reviews_amount'].fillna(0).astype(float)


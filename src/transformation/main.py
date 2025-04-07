import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import pandas as pd
from datetime import datetime
from sqlalchemy.orm import Session
from src.database.models import Sneaker
from src.database.db import engine

#Set the path for the JSONL file
df = pd.read_json('../data/data.jsonl', lines=True)

# Set pandas to display all columns
pd.options.display.max_columns = None

#Add the column _source with a fixed value
df['_source'] = "https://lista.mercadolivre.com.br/tenis-corrida-masculino"

#Add the column _data_coleta with the current date and time
df['_data_coleta'] = datetime.now ()

#Handle null values for numeric and text columns
df['old_price_brl'] = df['old_price_brl'].fillna(0).astype(float)
df['old_price_cents'] = df['old_price_cents'].fillna(0).astype(float)
df['new_price_brl'] = df['new_price_brl'].fillna(0).astype(float)
df['new_price_cents'] = df['new_price_cents'].fillna(0).astype(float)
df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(float)

#Remove the parentheses from the 'reviews_amount' column
df['reviews_amount'] = df['reviews_amount'].str.replace('[\\(\\)]', '', regex=True)
df['reviews_amount'] = df['reviews_amount'].fillna(0).astype(int)

#Handle prices as floats and calculate the total values
df['old_price'] = df['old_price_brl'] + df['old_price_cents'] / 100
df['new_price'] = df['new_price_brl'] + df['new_price_cents'] / 100

# Remove the old price columns
df.drop(columns=['old_price_brl', 'old_price_cents', 'new_price_brl', 'new_price_cents'], inplace=True)

# Insert into the database
with Session(engine) as session:
    session.query(Sneaker).delete()
    session.commit()
    for _, row in df.iterrows():
        sneaker = Sneaker(
            brand=row['brand'],
            name=row['name'],
            reviews_amount=row['reviews_amount'],
            reviews_rating_number=row['reviews_rating_number'],
            new_price=row['new_price'],
            old_price=row['old_price'],
            _source=row['_source'],
            _data_coleta=row['_data_coleta']
        )
        session.add(sneaker)
    session.commit()

print("Data inserted successfully!")
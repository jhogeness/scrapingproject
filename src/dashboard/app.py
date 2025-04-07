from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Load variables from .env
load_dotenv()

# Connect to the database using the variables
DB_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"

# Create SQLAlchemy engine
engine = create_engine(DB_URL)

# Execute the query and load into DataFrame
df = pd.read_sql_query("SELECT * FROM sneakers", engine)

# Application title
st.title("Market Research - Sports Sneakers on Mercado Livre")

# Improve layout with KPI columns
st.subheader('Main System KPIs')
col1, col2, col3 = st.columns(3)

# KPI 1: Total number of items
total_items = df.shape[0]
col1.metric(label='Total Number of Items', value=total_items)

# KPI 2: Number of unique brands
unique_brands = df['brand'].nunique()
col2.metric(label='Number of Unique Brands', value=unique_brands)

# KPI 3: Average new price (in BRL)
average_new_price = df['new_price'].mean()
col3.metric(label='Average New Price (R$)', value=f'{average_new_price:.2f}')

# Most common brands found up to the 10th page
st.subheader('Most Common Brands Found up to the 10th Page')
col1, col2 = st.columns([4, 2])
top_10_pages_brands = df['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_10_pages_brands)
col2.write(top_10_pages_brands)

# Average price by brand
st.subheader('Average Price by Brand')
col1, col2 = st.columns([4, 2])
df_non_zero_prices = df[df['new_price'] > 0]
average_price_by_brand = df_non_zero_prices.groupby('brand')['new_price'].mean().sort_values(ascending=False)
col1.bar_chart(average_price_by_brand)
col2.write(average_price_by_brand)

# Satisfaction by brand
st.subheader('Satisfaction by Brand')
col1, col2 = st.columns([4, 2])
df_non_zero_reviews = df[df['reviews_rating_number'] > 0]
satisfaction_by_brand = df_non_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
col1.bar_chart(satisfaction_by_brand)
col2.write(satisfaction_by_brand)

# 🏃‍♂️ Market Research: Men's Running Shoes on Mercado Livre

This project scrapes data from the Mercado Livre website about men's running shoes using Scrapy and displays it in an interactive dashboard built with Streamlit. The data is stored in a PostgreSQL database for further analysis and visualization.

---

## 📦 Features

- Automatic data scraping with Scrapy (brand, name, old/new prices, ratings, review counts).
- Data storage in a PostgreSQL database.
- Interactive dashboard with key metrics and charts using Streamlit.
- KPIs: total items, number of unique brands, average new price.
- Visual insights on the most common brands found on the first 10 pages.

---

## 🛠 Technologies Used

- 🕷 **Scrapy** – for web scraping.
- 🐘 **PostgreSQL** – relational database.
- 🐍 **SQLAlchemy** – ORM for database management.
- 🌱 **Dotenv** – for environment variable management.
- 📊 **Streamlit** – for building the data dashboard.
- 🐼 **Pandas** – for data manipulation.

---

## ⚙️ How to Run the Project

To run the web scraping

```bash
scrapy crawl mercadolivre -o ../../data/data.jsonl
```

To run PANDAS (inside the src folder)

```bash
python transformation/main.py
``` 

To run Dashboard (inside the src folder)

```bash
streamlit run dashboard/app.py
``` 
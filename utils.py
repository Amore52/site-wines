from datetime import datetime
import pandas as pd
from collections import defaultdict



def load_data(file_path):
    return pd.read_excel(file_path, na_values=[' '], keep_default_na=False)


def organize_products(data_file):
    products = defaultdict(list)
    for index, row in data_file.iterrows():
        category = row['Категория']
        wine_info = {
            'Название': row['Название'],
            'Сорт': row['Сорт'],
            'Цена': row['Цена'],
            'Картинка': row['Картинка'],
            'Акция': row['Акция']
        }
        products[category].append(wine_info)
    return products


def get_years_since_foundation(foundation_date):
    today = datetime.today().date()
    difference = (today - foundation_date).days // 365
    return difference

def get_year_form(years):
    last_digit = years % 10
    last_two_digits = years % 100

    if last_two_digits in [11, 12, 13, 14]:
        return "лет"
    elif last_digit == 1:
        return "год"
    elif last_digit in [2, 3, 4]:
        return "года"
    else:
        return "лет"




import argparse
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime
from utils import load_data, organize_products, get_years_since_foundation, get_year_form
from dotenv import load_dotenv



def render_template(products, years, year_form):
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    rendered_page = template.render(
        year_creation=years,
        years_form=year_form,
        products=products
    )
    return rendered_page


def save_rendered_page(rendered_page, output_file):
    with open(output_file, 'w', encoding="utf8") as file:
        file.write(rendered_page)


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Загрузчик данных веб-сайта вин.")
    parser.add_argument('--data_file', type=str, default=os.getenv('DATA_FILE'),
                        help='Путь до таблицы с данными.')
    args = parser.parse_args()
    data_file = load_data(args.data_file)
    products = organize_products(data_file)
    foundation_date = datetime(1919, 1, 1).date()
    years = get_years_since_foundation(foundation_date)
    year_form = get_year_form(years)
    rendered_page = render_template(products, years, year_form)
    save_rendered_page(rendered_page, 'index.html')

    server = HTTPServer(('127.0.0.1', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
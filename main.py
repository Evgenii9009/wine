import pandas
import collections
import datetime


from functions import correct_ending, counting_years, create_parser
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    ongoing_date = datetime.datetime.now()
    delta_years = counting_years(ongoing_date)
    winery_text = correct_ending(delta_years)

    path = create_parser().parse_args().datapath
    wines_excel = pandas.read_excel(path)
    wines_excel = wines_excel.fillna("")
    wines = wines_excel.to_dict(orient='records')
    wine_collection = collections.defaultdict(list)
    for wine in wines:
        wine_type = wine["Категория"]
        wine_collection[wine_type].append(wine)
    rendered_page = template.render(
        wine_collection=wine_collection,
        winery_age=winery_text
        )
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()

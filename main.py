import datetime
import pandas 
import collections

from functions import correct_ending
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')
winery_text = correct_ending()

wines_excel = pandas.read_excel('wine3.xlsx')
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

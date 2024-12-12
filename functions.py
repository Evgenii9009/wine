import argparse
import pathlib


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('datapath', type=pathlib.Path,  default='wine3.xlsx')
    return parser


def counting_years(date):
    delta_years = date.year - 1920
    return delta_years


def correct_ending(delta_years):
    text_template = "Уже {} {} с вами"
    decades = delta_years % 100
    if 10 < decades < 21:
        winery_age = text_template.format(delta_years, "лет")
    else:
        last_number = decades % 10
        if last_number == 1:
            winery_age = text_template.format(delta_years, "год")
        elif 1 < last_number < 5:
            winery_age = text_template.format(delta_years, "года")
        else:
            winery_age = text_template.format(delta_years, "лет")
    return winery_age

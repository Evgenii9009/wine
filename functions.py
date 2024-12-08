import datetime
import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default='wine3.xlsx')
    return parser

def years_passed():
    ongoing_date = datetime.datetime.now()
    delta_years = int(ongoing_date.year) - 1920
    return delta_years


def correct_ending(delta_years):
    text_template = "Уже "+str(delta_years)+" {} с вами"
    decades = delta_years%100
    if 10<decades<21:
        winery_age = text_template.format("лет")
    else:
        last_number = decades%10
        if last_number==1:
            winery_age = text_template.format("год")
        elif 1<last_number<5:
            winery_age = text_template.format("года")
        else:
            winery_age = text_template.format("лет")
    return winery_age

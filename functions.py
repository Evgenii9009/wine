import datetime


def correct_ending():
    ongoing_date = datetime.datetime.now()
    delta_years = int(ongoing_date.year) - 1920
    decades = delta_years%100
    text_template = "Уже "+str(delta_years)+" {} с вами"
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

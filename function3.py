def date_parser(list_dates):
    c = []
    for i in list_dates:
        dates = i[:10] # the date from the datetime string is only made up of 9 characters
        c.append(dates)
    return c

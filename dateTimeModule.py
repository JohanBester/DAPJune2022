import datetime

"""
    %a = weekday, abbreviation
    %A = weekday, full name
    %w = weekday, number
    %d = day of month
    %b = month, abbreviation
    %B = month, full name
    %m = month as a number
    %y = year, short
    %Y = year, full

"""

x = datetime.datetime.now()
print("Current date and time ...", x)

y = datetime.datetime(2022, 8, 15)
print("Specified date ...", y)

w = datetime.datetime.now()
print("Year only ... ", w.year)
print("Full weekday ... ", w.strftime("%A"))

v = datetime.datetime(2018, 6, 1)
print("Full month ... ", v.strftime("%B"))

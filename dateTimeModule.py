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

# Current date and time
x = datetime.datetime.now()
print("Current date and time ...", x)

# Specify a Specified date
y = datetime.datetime(2022, 8, 15)
print("Specified date ...", y)

# Get year or day of the full dateTime
w = datetime.datetime.now()
print("Year only ... ", w.year)
print("Full weekday ... ", w.strftime("%A"))

# Get full month of the full dateTime
v = datetime.datetime(2018, 6, 1)
print("Full month ... ", v.strftime("%B"))

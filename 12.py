#Write a Python program that prints the calendar for a given month and year.
#Note : Use 'calendar' module.

import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y,m))
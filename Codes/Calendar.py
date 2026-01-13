import calendar
#program to print calendar of a given month and year.
year = int(input("Enter year: "))
month = int(input("Enter Month (1-12): "))
print(f"Calendar for {month} in {year} year is: ")
print(calendar.month(year, month))
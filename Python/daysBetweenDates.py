# The daysBetweenDates function takes two input dates in the form of
# (year1, month1, day1, year2, month2, day2) and then determines the number
# of days that have passed between them. First date must be older than second.

## An array with amount of days in each month, starting with Janurary.
daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
## Determines if the input year is a Leap Year or not.
def leapYearChecker(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
## Returns the number of days in a year, taking into account Leap Years.
def daysInYear(year):
    if leapYearChecker(year) == True:
        return 366
    else:
        return 365
## Builds an array of all the years between two different years, excluding the input years.
def yearFinder(year1, year2):
    yearCount = year1 + 1
    yearArray = []
    while yearCount < year2:
        yearArray.append(yearCount)
        yearCount = yearCount + 1
    return yearArray
## Calculates the days that have passed from the start of the year to the given date.
def daysIntoYear(year, month, day):
    daysIn = day
    monthArray = daysOfMonths[0:(month-1)]
    for monthItem in monthArray:
        daysIn = daysIn + monthItem
    if leapYearChecker(year) == True and month > 2:
        daysIn = daysIn + 1
    return daysIn
## Calculates the days that remain in a year after the given date.
def daysLeftInYear(year, month, day):
    return (daysInYear(year) - daysIntoYear(year, month, day))
## Finds the number of days between two dates. First date needs to be older than second date.
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    totalDays = 0
    if year1 != year2 and (year1 + 1) != year2:
        yearArray = yearFinder(year1, year2)
        for yearItem in yearArray:
            totalDays = totalDays + daysInYear(yearItem)
        totalDays = totalDays + daysLeftInYear(year1, month1, day1) + daysIntoYear(year2, month2, day2)
    elif (year1 + 1) == year2:
        totalDays = daysLeftInYear(year1, month1, day1) + daysIntoYear(year2, month2, day2)
    else:
        totalDays = (daysInYear(year1) - daysLeftInYear(year2, month2, day2)) - daysIntoYear(year1, month1, day1)
    return totalDays

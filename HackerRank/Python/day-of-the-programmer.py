try:
    from raw_input import input
except ImportError:
    pass

def gregorian_leap_year(year):
    if (year % 400 == 0) or ((year % 4 == 0) and year % 100 != 0):
        return True
    else:
        return False

def julian_leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False

def is_leap_year(system, year):
    if system == "gregorian":
        return gregorian_leap_year(year)
    else:
        return julian_leap_year(year)

def dayOfProgrammer(year):
    leap_year = False
    if year == 1918:
        return "26.09.{}".format(year)
    elif year > 1918:
        leap_year = is_leap_year("gregorian", year)
    else:
        leap_year = is_leap_year("julian", year)

    if leap_year:
        return "12.09.{}".format(year)
    else:
        return "13.09.{}".format(year)


if __name__ == '__main__':
    year = int(input().strip())

    result = dayOfProgrammer(year)
    print(result)
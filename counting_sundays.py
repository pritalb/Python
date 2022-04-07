# You are given the following information, but you may prefer to do some research for yourself.

# *   1 Jan 1900 was a Monday.
# *   Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
# *   A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def is_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


def counting_sundays(start_year, end_year, jan1_dotw_start_year):
    # number of sundays that fall on 1st of the month with respect to the dotw on jan 1. index[0..6] -> day of the week[sun..sat]
    sundays_non_leap = [2, 2, 2, 1, 3, 1, 1]
    sundays_leap = [3, 2, 1, 2, 2, 1, 1]
    jan1 = jan1_dotw_start_year
    sundays_count = 0
    
    for year in range(start_year, end_year + 1):
        if is_leap(year):
            sundays_count += sundays_leap[jan1 % 7]
            jan1 += 2
        else:
            sundays_count += sundays_non_leap[jan1 % 7]
            jan1 += 1
            
    return sundays_count

print(counting_sundays(1901, 2000, 2))
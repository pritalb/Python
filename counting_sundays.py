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

# def date_tuple(date_str):
#     # converts a 'yyyy-mm-dd' format date to a tuple of ints -> (year, month, day)
#     date_list_format = date_str.split('-')
#     return tuple(map(int, date_list_format))

# def counting_days(start_date, end_date):
#     days_in_months = [
#         31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31,
#     ]
#     start_date_tup = date_tuple(start_date)
#     end_date_tup = date_tuple(end_date)

#     year_diff = end_date_tup[0] - start_date_tup[0]
#     month_diff = end_date_tup[1] - start_date_tup[1]
#     day_diff = end_date_tup[2] - start_date_tup[2]

#     days_between_years = year_diff * 365 + (year_diff // 4)


# def counting_sundays(start_date, end_date):
#     pass

# print(counting_days('2022-01-01', '2022-02-01'))
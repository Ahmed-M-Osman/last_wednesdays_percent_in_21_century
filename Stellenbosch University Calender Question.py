wed_count = 0
last_wed_count = 0


# Got this function from a stck overflow question and modified it
def eomday(year, month):
    """returns the number of days in a given month"""
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_code = [6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    m_code = month_code[month - 1]
    d = days_per_month[month - 1]
    if month == 2 and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        d = 29
        m_code = 1
    if month == 1 and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        m_code = 5
        
    return d, m_code

for year in range(1, 101):
    y_code = (int(year/4) + year) % 7
    
    for month in range(1, 13):
        day, mo_code = eomday(year, month)
        
        for i in range(1,day+1):
            all_days_code = (y_code + mo_code + i) % 7
            if all_days_code == 3:
                wed_count += 1
        
        last_week_day_code = (y_code + mo_code + day) % 7
        
        if last_week_day_code == 3:
            last_wed_count += 1
        
per_of_last_wed = (last_wed_count/wed_count)*100
print(per_of_last_wed)
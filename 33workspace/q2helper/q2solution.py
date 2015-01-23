import re

# Use day_dict and is_leap_year in your tomorrow function

day_dict ={ 1 : 31,
            2 : 28,
            3 : 31,
            4 : 30,
            5 : 31,
            6 : 30,
            7 : 31,
            8 : 31,
            9 : 30,
           10 : 31, 
           11 : 30,
           12 : 31} 

def is_leap_year(year:int)->bool:
    return (year%4 == 0 and year%100 != 0) or year%400==0

def days_in(month:int,year:int)->int:
    return (29 if month==2 and is_leap_year(year) else day_dict[month])

def tomorrow(date:str)->str:
    mdate= re.match(r'(1[0-2]|[1-9])/([1-3][0-1]|[1-2][0-9]|0?[1-9])/([0-9]{4}|[0-9]{2})$', date)
    assert mdate, 'Invalid pattern. The date pattern does not match.'
    month, day, year = mdate.group(1,2,3)
    if len(year) == 2:
        year = int(year)+2000
    month, day, year = int(month), int(day), int(year)
    max_days = days_in(month, year)
    assert day <= max_days, 'Invalid day. The day is too big for month.'
    if day == max_days:
        if month == 12:
            month,day, year = 1,1, 1+year
        else:
            month,day = month+1,1
    else:
        day+=1
    
    return '{mm}/{dd}/{yyyy}'.format(mm = month, dd = day, yyyy = year)
            
            
if __name__ == '__main__':
    import driver, prompt,traceback
    while True:
        date = prompt.for_string('Enter a date to test (quit to start driver)')
        if date == 'quit':
            break;
        try:
            print('tomorrow=',tomorrow(date))
        except:
            print('tomorrow raised exception')
            traceback.print_exc()
        
    driver.driver()

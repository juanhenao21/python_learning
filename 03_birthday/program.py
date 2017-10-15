import datetime

def print_header():
    print('--------------------------------')
    print('         Birthday app' )
    print('--------------------------------')
    print()

def get_birthday_from_user():
    print('When were you born? ')
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))

    birthday = datetime.date(year,month,day)
    return birthday

def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    
    dt = this_year - target_date
    return dt.days

def compute_future_days_birthday(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)

    dt = this_year - target_date

    if (dt.days > 0):
        return dt.days
    else:
        next_year = datetime.date(target_date.year + 1, original_date.month, original_date.day )
        dtf = next_year - target_date
        return dtf.days


def print_birthday_information(days):
    if (days < 0):
        print("You had your birthday {} days ago this year." .format(-days))
    elif (days > 0):
        print('Your birthday is in {} days!' .format(days))
    else:
        print("Happy Birthday!!!")

def print_future_birthday(future_days):
    if (future_days == 0):
        print('Happy Birthday!!!')
    else:
        print('Your birthday is in {} days!' .format(future_days))

def main():
    print_header()
    bday = get_birthday_from_user()
    today = datetime.date.today() 
    number_of_days = compute_days_between_dates(bday,today)
    number_of_future_days = compute_future_days_birthday(bday,today)
    print_birthday_information(number_of_days)
    print_future_birthday(number_of_future_days)

main()
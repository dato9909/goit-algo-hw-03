from datetime import datetime, timedelta


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "David K", "birthday": "1990.03.17" }
]
#print(users)


def first_func(users):

    prepared_users = []

    for user in users:
        try:
                birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
                prepared_users.append({'name' : user['name'], 'birthday' : birthday})
        except ValueError:
                print(f'Неккоректна дата народження для користувача {user['name']}')
    return prepared_users
 
   


def find_next_weekday(d , weekday: int):
    # Функция для нахождения следующего заданного дня недели после заданной даты
    # d : datatime.date - начальная дата
    # weekday : int - день недели от 0 до 6

    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: #Если день рождения уже прошел
        days_ahead += 7
    return d + timedelta(days = days_ahead)



def get_upcoming_birthdays(days=7):
    
    today = datetime.today().date()
    upcoming_birthdays = []
    
    prepared_users = first_func(users)

    for user in prepared_users:
        birthday_this_year = user["birthday"].replace(year = today.year ) #1985 -> 2024 
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year+1)
        
        if 0 <= (birthday_this_year - today).days <= days:
            if birthday_this_year.weekday() <= 5: # Суббота, воскресенье
                birthday_this_year = find_next_weekday(birthday_this_year , 0) # понедельник
            
            congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d')
            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': congratulation_date_str
            })
    print(upcoming_birthdays)

get_upcoming_birthdays()
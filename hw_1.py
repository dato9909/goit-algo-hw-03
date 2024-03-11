from datetime import datetime


def get_days_from_today(date):
    try:
        a = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.today()
        delta = current_date.day - a.day
        return delta
    except ValueError:
        print('Неправильнный ввод данных')

get_days_from_today()
    
        
